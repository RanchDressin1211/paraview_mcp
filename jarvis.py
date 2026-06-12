#!/usr/bin/env python3
"""
Jarvis Voice Command Bridge.
Listens to the microphone via WhisperLiveKit server and sends commands
starting with 'jarvis' and ending with 'end command' to Claude Code.
"""

import asyncio
import sys
import json
import os
from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ResultMessage, ClaudeAgentOptions

try:
    import pyaudio
except ImportError:
    print("Error: pyaudio is not installed. Please install it with: pip install pyaudio")
    sys.exit(1)

try:
    import websockets
except ImportError:
    print("Error: websockets is not installed. Please install it with: pip install websockets")
    sys.exit(1)

# Audio configuration - must match WhisperLiveKit server
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_DURATION = 0.1
CHUNK_SIZE = int(RATE * CHUNK_DURATION)

def generate_wav_header(sample_rate=16000, bits_per_sample=16, channels=1, data_size=0xFFFFFFFF):
    data_size = 0xFFFFFFFF - 36
    byte_rate = sample_rate * channels * (bits_per_sample // 8)
    block_align = channels * (bits_per_sample // 8)
    header = bytearray()
    header.extend(b'RIFF')
    header.extend((36 + data_size).to_bytes(4, 'little'))
    header.extend(b'WAVE')
    header.extend(b'fmt ')
    header.extend((16).to_bytes(4, 'little'))
    header.extend((1).to_bytes(2, 'little'))
    header.extend(channels.to_bytes(2, 'little'))
    header.extend(sample_rate.to_bytes(4, 'little'))
    header.extend(byte_rate.to_bytes(4, 'little'))
    header.extend(block_align.to_bytes(2, 'little'))
    header.extend(bits_per_sample.to_bytes(2, 'little'))
    header.extend(b'data')
    header.extend(data_size.to_bytes(4, 'little'))
    return bytes(header)

async def send_to_claude(command, client):
    """
    Sends the extracted command to Claude using the SDK.
    """
    print(f"\n🚀 Sending to Claude: {command}")
    try:
        await client.query(command)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print("Claude Response to: ", command, ". \nis: ", block.text)
    except Exception as e:
        print(f"Failed to send command to Claude: {e}")

async def main():
    print("Connecting to WhisperLiveKit server at ws://localhost:8000/asr...")
    
    options = ClaudeAgentOptions(
        mcp_servers={
            "paraview_mcp": {
                "command": "docker",
                "args": ["run", "-i", "--rm", "--name", "paraview_mcp", "paraview_mcp"],
                "env": {},
            }
        },
        allowed_tools=["mcp__paraview_mcp__*"]
    )

    # Create a single SDK client to be reused across all commands
    async with ClaudeSDKClient(options=options) as client:    
        
        # use ping_interval and ping_timeout to prevent 1011 keepalive errors
        async with websockets.connect(
            "ws://localhost:8000/asr",
            ping_interval=20,
            ping_timeout=20
        ) as websocket:
            print("Connected. Listening for 'jarvis ... end command'...")

            config_raw = await websocket.recv()
            config_msg = json.loads(config_raw)
            use_pcm = config_msg.get("useAudioWorklet", False)
            mode = config_msg.get("mode", "full")

            capturing_command = False
            # Track the index of the last processed 'end command' to avoid repeats
            last_processed_end_index = -1

            async def receive_and_process():
                nonlocal capturing_command, last_processed_end_index
                try:
                    async for raw_msg in websocket:
                        data = json.loads(raw_msg)

                        lines = data.get("lines", [])
                        buffer = data.get("buffer_transcription", "")

                        text_parts = [line["text"] for line in lines if line.get("text")]
                        full_text = " ".join(text_parts) + " " + buffer
                        lower_text = full_text.lower()

                        # Trigger detection: only if not already capturing
                        if not capturing_command and "jarvis" in lower_text:
                            capturing_command = True
                            print("\n🎙️ Jarvis listening...")

                        if capturing_command:
                            if "end command" in lower_text:
                                # Find the last 'jarvis' and the first 'end command' after it
                                last_jarvis_idx = lower_text.rfind("jarvis")
                                first_end_idx = lower_text.find("end command", last_jarvis_idx)

                                # Only process if this 'end command' is newer than the last one we handled
                                if first_end_idx != -1 and first_end_idx > last_processed_end_index:
                                    command = full_text[last_jarvis_idx + 6 : first_end_idx].strip()
                                    asyncio.create_task(send_to_claude(command, client))

                                    last_processed_end_index = first_end_idx
                                    capturing_command = False
                                    print("\n✅ Command processed. Listening again...")

                        if buffer:
                            print(f"\rListening... {buffer}", end="", flush=True)

                except Exception as e:
                    print(f"\nReceiver error: {e}")

            recv_task = asyncio.create_task(receive_and_process())

            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK_SIZE
            )

            if not use_pcm:
                await websocket.send(generate_wav_header())

            try:
                while True:
                    data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
                    await websocket.send(data)
            except KeyboardInterrupt:
                await websocket.send(b"")
            finally:
                stream.stop_stream()
                stream.close()
                audio.terminate()
                await recv_task

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
