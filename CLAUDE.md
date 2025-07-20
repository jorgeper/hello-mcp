# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server implementation that demonstrates basic MCP functionality. It serves as a learning example for building MCP servers using the FastMCP framework, exposing 4 tools, 1 resource, and 1 prompt.

## Development Environment

### Virtual Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
- `mcp[cli]>=1.0.0` - Core MCP framework with FastMCP
- `fastapi>=0.115.0` - For HTTP API testing wrapper

## Architecture

### Core Components
- `hello_server.py` - Main MCP server using FastMCP framework
- `test_server.py` - Direct tool testing without client (imports functions directly)
- `run_stdio.py` - stdio transport for MCP clients (Claude Desktop, Cursor)
- `run_http.py` - HTTP/REST API wrapper for curl testing
- `run_sse.py` - SSE transport server for web clients

### MCP Server Pattern
The server follows the FastMCP pattern where:
- Server is initialized with `FastMCP(name, version, description)`
- Tools are decorated functions using `@mcp.tool()` with full type hints
- Resources use `@mcp.resource(uri_pattern)` for dynamic content
- Prompts use `@mcp.prompt()` for reusable templates
- Server runs with `mcp.run(transport="stdio")` for client integration

### Exposed Capabilities
- **4 Tools**: `say_hello`, `get_greeting_info`, `create_custom_greeting`, `list_available_greetings`
- **1 Resource**: `greeting://template/{greeting_type}` - greeting templates
- **1 Prompt**: `greeting_prompt` - reusable greeting prompt template

## Development Commands

### Local Development
```bash
# Direct tool testing (recommended for development)
python test_server.py

# HTTP API testing with FastAPI wrapper
python run_http.py
# Then test with: curl http://localhost:8000/tools

# Run MCP server for clients (Claude Desktop, Cursor)
python run_stdio.py

# SSE transport server (for web clients)
python run_sse.py
```

### Docker Development
```bash
# Build the Docker image
docker build -t hello-mcp .

# Run HTTP transport (for curl testing)
docker run -p 8000:8000 hello-mcp

# Run stdio transport (for MCP clients)
docker run -it hello-mcp python run_stdio.py

# Run tests in container
docker run hello-mcp python test_server.py

# Development with mounted source code
docker run -p 8000:8000 -v $(pwd):/app hello-mcp

# Interactive debugging
docker run -it hello-mcp /bin/bash
```

### Client Integration
Detailed setup instructions are in `how-to-run-mcp.md` for:
- Claude Desktop configuration (requires absolute paths)
- Cursor IDE integration
- Custom MCP client development

### Linting/Type Checking
This project currently has no linting or type checking commands configured. The code uses type hints throughout but lacks formal validation tools.