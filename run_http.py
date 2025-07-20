#!/usr/bin/env python3
"""
HTTP/SSE runner for the MCP server.
Allows testing with curl or other HTTP clients.
"""

import os
from hello_server import mcp

if __name__ == "__main__":
    # Set the port via environment variable (FastMCP uses uvicorn defaults)
    os.environ["UVICORN_PORT"] = "8000"
    
    print("Starting Hello World MCP Server with HTTP/SSE transport...")
    print("Server will be available at: http://localhost:8000")
    print("Test with curl commands from how-to-run-mcp.md")
    print("-" * 50)
    
    # Run with SSE transport
    mcp.run(transport="sse")