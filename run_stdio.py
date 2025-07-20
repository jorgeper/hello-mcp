#!/usr/bin/env python3
"""
Runs the MCP server in stdio mode for client integration.
This is the transport mode used by Claude Desktop, Cursor, and other MCP clients.
"""

from hello_server import mcp

if __name__ == "__main__":
    print("Starting Hello MCP Server in stdio mode...", file=__import__('sys').stderr)
    print("This server communicates via stdin/stdout for MCP client integration.", file=__import__('sys').stderr)
    print("Use this mode with Claude Desktop, Cursor, or other MCP clients.", file=__import__('sys').stderr)
    print("-" * 60, file=__import__('sys').stderr)
    
    # Run the server using stdio transport
    mcp.run(transport="stdio")