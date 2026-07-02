#!/usr/bin/env python3
"""
Jarvis Voice Command Bridge.
Listens to the microphone via WhisperLiveKit server and sends commands
starting with 'jarvis' and ending with 'pronto' to Claude Code.
"""
import asyncio
import sys
import json
import time
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

async def send_to_claude(command, client, state):
    """Sends command to Claude, tracks time/tokens, and blocks new input until done."""
    state["is_claude_busy"] = True
    print(f"\n🚀 Sending to Claude: '{command}'")
    
    start_time = time.time()
    token_estimate = 0
    
    # Background task to update the console on the same line
    async def loading_indicator():
        try:
            while True:
                elapsed = time.time() - start_time
                print(f"\r⏳ Claude processing... Time: {elapsed:.1f}s | Est. Tokens: {token_estimate}", end="", flush=True)
                await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            pass

    indicator_task = asyncio.create_task(loading_indicator())
    full_response = ""

    try:
        await client.query(command)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        full_response += block.text
                        token_estimate = len(full_response) // 4
    except Exception as e:
        print(f"\n❌ Failed to send command to Claude: {e}")
    finally:
        # Stop the loading animation and clear its line completely
        indicator_task.cancel()
        print("\r" + " " * 70 + "\r", end="", flush=True)

    # Print final output safely
    print(f"\n🤖 Claude Response:\n{full_response.strip()}")
    
    # Unlock Claude so Jarvis can begin listening to fresh audio inputs again
    state["is_claude_busy"] = False
    state["capturing_command"] = False
    print("\n✅ Command processed. Jarvis is ready to listen for 'jarvis ... pronto'...")

async def main():
    print("Initializing Jarvis Bridge...")
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

    async with ClaudeSDKClient(options=options) as client:    
        print("Connecting to WhisperLiveKit server at ws://localhost:8000/asr...")
        async with websockets.connect(
            "ws://localhost:8000/asr",
            ping_interval=20,
            ping_timeout=20
        ) as websocket:
            
            config_raw = await websocket.recv()
            config_msg = json.loads(config_raw)
            use_pcm = config_msg.get("useAudioWorklet", False)
            
            # Shared thread-safe state context
            state = {
                "capturing_command": False,
                "last_processed_end_index": -1,
                "is_claude_busy": False
            }

            # Instantiate our advanced AsyncIO Communication Queue
            queue = asyncio.Queue()

            async def receiver():
                """Background task: Continuously feeds the queue with fresh server data."""
                try:
                    async for raw_msg in websocket:
                        # Flush any older, unhandled text objects to stay perfectly synchronized
                        while not queue.empty():
                            try:
                                queue.get_nowait()
                            except asyncio.QueueEmpty:
                                break
                        await queue.put(raw_msg)
                except Exception as e:
                    print(f"\nReceiver error: {e}")

            async def processor():
                """Background task: Wakes up instantly to parse new text data when it hits the queue."""
                while True:
                    raw_msg = await queue.get()
                    
                    # Do not process anything new if Claude is currently running an action
                    if state["is_claude_busy"]:
                        continue

                    try:
                        data = json.loads(raw_msg)
                        lines = data.get("lines", [])
                        buffer = data.get("buffer_transcription", "")
                        text_parts = [line["text"] for line in lines if line.get("text")]
                        full_text = " ".join(text_parts) + " " + buffer
                        lower_text = full_text.lower()

                        # If the server clears out old history segments, reset our offset tracking index
                        if len(lower_text) < state["last_processed_end_index"]:
                            state["last_processed_end_index"] = -1

                        # Slice our lookup window so we skip past anything we have already run
                        search_start = max(0, state["last_processed_end_index"])
                        visible_text = lower_text[search_start:]

                        if not state["capturing_command"] and "jarvis" in visible_text:
                            state["capturing_command"] = True
                            print("\n🎙️ Jarvis listening...")

                        if state["capturing_command"]:
                            # Find the wake word relative to our timeline window
                            last_jarvis_idx = lower_text.rfind("jarvis")
                            if last_jarvis_idx != -1 and last_jarvis_idx >= search_start:
                                first_end_idx = lower_text.find("pronto", last_jarvis_idx)
                                
                                # Found a complete phrase structure!
                                if first_end_idx != -1:
                                    command = full_text[last_jarvis_idx + 6 : first_end_idx].strip()
                                    
                                    # Move our index forward past "pronto" IMMEDIATELY so it can't loop
                                    state["last_processed_end_index"] = first_end_idx + len("pronto")
                                    state["capturing_command"] = False
                                    
                                    # Execute command
                                    asyncio.create_task(send_to_claude(command, client, state))

                        if buffer and state["capturing_command"] and not state["is_claude_busy"]:
                            print(f"\rListening... {buffer}", end="", flush=True)
                                
                    except Exception as e:
                        print(f"\nProcessing error: {e}")

            # Fire off data pipeline engines
            recv_task = asyncio.create_task(receiver())
            proc_task = asyncio.create_task(processor())

            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK_SIZE
            )
            
            if not use_pcm:
                await websocket.send(generate_wav_header())

            print("\n✅ Systems Online. Jarvis is ready to listen for 'jarvis ... pronto'...")

            try:
                while True:
                    data = await asyncio.get_event_loop().run_in_executor(
                        None, stream.read, CHUNK_SIZE, False
                    )
                    await websocket.send(data)
                    await asyncio.sleep(0)
            except KeyboardInterrupt:
                await websocket.send(b"")
            finally:
                stream.stop_stream()
                stream.close()
                audio.terminate()
                recv_task.cancel()
                proc_task.cancel()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutting down Jarvis...")