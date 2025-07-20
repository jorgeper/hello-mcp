# Hello World MCP Server

A simple example of a Model Context Protocol (MCP) server that demonstrates basic functionality with greeting tools.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   
   Choose one of three transport methods:
   
   ```bash
   # For MCP clients (Claude Desktop, Cursor) - stdio transport
   python run_stdio.py
   
   # For HTTP/REST API testing with curl
   python run_http.py
   
   # For SSE transport (web clients)
   python run_sse.py
   ```

3. **Test the server:**
   ```bash
   # Test the tools without a client
   python test_server.py
   
   # Test with HTTP API and curl
   python run_http.py
   # Then: curl http://localhost:8000/tools
   ```

## Features

This server provides:
- 4 tools for creating and managing greetings
- 1 resource for greeting templates
- 1 prompt for generating greetings

## Documentation

See [how-to-run-mcp.md](how-to-run-mcp.md) for detailed instructions on:
- Running the server locally
- Testing with various methods
- Integrating with Claude Desktop
- Troubleshooting common issues

## Project Structure

```
hello-mcp/
├── hello_server.py              # Main MCP server implementation
├── test_server.py               # Test script for tools
├── run_stdio.py                 # stdio transport for MCP clients (Claude Desktop, Cursor)
├── run_http.py                  # HTTP API wrapper for curl testing
├── run_sse.py                   # SSE transport for web clients
├── requirements.txt             # Python dependencies
├── how-to-run-mcp.md           # Detailed setup and testing guide
├── claude_desktop_config_example.json  # Example Claude Desktop configuration
├── README.md                    # This file
└── CLAUDE.md                    # Claude Code guidance file
```

## Transport Methods

This server can run in three different modes:

1. **stdio transport** (`run_stdio.py`) - For MCP clients like Claude Desktop and Cursor
2. **HTTP transport** (`run_http.py`) - REST API for testing with curl commands
3. **SSE transport** (`run_sse.py`) - Server-Sent Events for web clients (requires MCP-compatible web client)

## Available Tools

1. **say_hello(name)** - Basic greeting
2. **get_greeting_info()** - Server information
3. **create_custom_greeting(name, type, include_time)** - Customized greetings
4. **list_available_greetings()** - List greeting types

## License

This is an example project for learning MCP.
