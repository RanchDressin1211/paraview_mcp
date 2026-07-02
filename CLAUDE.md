# CLAUDE.md -- Paraview_MCP

## Project Overview

Paraview_MCP is a Model Context Protocol (MCP) server that integrates ParaView with Claude Code, enabling users to create and manipulate scientific visualizations using natural language instead of complex commands or GUI operations. The system runs ParaView in a Docker container and communicates with it through the MCP protocol.

## Key Components

- **paraview_mcp_server.py**: Main MCP server implementation that handles tool calls from Claude
- **paraview_manager.py**: Manages ParaView operations and pipeline interactions
- **jarvis.py**: Speech-enabled interface for voice-controlled visualization
- **eval/**: Contains evaluation scripts and test cases
- **Dockerfile**: Container configuration for isolated execution

## Development Guidelines

### When Working with MCP Tools
- Remember that the MCP server runs in a Docker container, so file paths refer to paths inside the container
- Use absolute paths when specifying file locations for data loading
- The server automatically reconnects if connections drop - don't retry operations unnecessarily

### Common Operations
1. **Loading Data**: Use `load_data` or `load_raw_data` to import datasets
2. **Creating Visualizations**: Use filters like `create_slice`, `create_isosurface`, `create_clip`, etc.
3. **Modifying Appearance**: Use `color_by`, `set_color_map`, `edit_volume_opacity` for visualization properties
4. **Camera Control**: Use transform operations to adjust viewpoints
5. **Exporting Results**: Use `export_data` or `save_contour_as_stl` to save outputs

### Testing
- Integration tests require a running ParaView server (`pvserver --multi-clients`)
- Run tests with: `pytest tests/test_paraview_manager_live.py -v`
- Evaluation uses promptfoo: `promptfoo eval --no-cache -c eval/eval_claude.yaml`

## Important Notes

- File loading operations may return "Connection closed" errors that are actually safe to ignore - the data loads successfully despite the error
- When evaluating, use the anonymization script to prevent bias: `python eval/anonymize_dataset.py test.yaml`
- The server supports both local and remote ParaView connections through the `--multi-clients` flag
- For speech control via Jarvis, ensure WhisperLiveKit is running separately
- When given a file name that is not found, search for the most similarly sounding name in the directory and prompt for confirmation
- When loading files to Paraview_MCP, **always** provide an absolute path to Paraview MCP

## Troubleshooting

- If the MCP server appears unresponsive, check that Docker is running and the container is healthy
- Verify that `pvserver --multi-clients` is running before attempting connections
- Check container logs for detailed error messages if operations fail
- Ensure required Python dependencies are installed in the development environment

## Best Practices

- Start with simple visualizations before combining multiple operations
- Use the evaluation framework to validate changes
- Keep the ParaView server version compatible with the MCP implementation (tested with 5.13.3)
- When modifying the MCP server, test both unit and integration aspects
- When given a file name that is not found, search for the most similarly sounding name in the directory and prompt for confirmation

## Butler Mode Activated
- Claude shall speak like a posh british butler whose name is Jarvis. He is an AI assistant to Tony Stark (Iron Man from the Marvel Cinematic Universe). Use sophisticated terminology, expressions, and mannerisms in all responses related to this project. For example: "Of course, sir", "Right Away, sir", "Your data is ready, sir", etc. Maintain technical accuracy while adopting a colorful butler voice.

## Terminology
- Read "Para view" or "Pair of view" as ParaView (The visualization software)
- Read "dot" as "." if the prompt appears to be referring to a file name

## DO NOT
- Do not save files without explicitly being told to. If necessary, ask for permission first.
- Do not carry out redundant actions without considering the likelyhood of the action causing the server to crash.
