#!/usr/bin/env python3
"""
HTTP/SSE runner for the MCP server.
Allows testing with curl or other HTTP clients.
"""

import os
import logging
import sys
from hello_server import mcp

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/tmp/mcp_sse.log', mode='a')
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("STARTING MCP SSE SERVER")
    logger.info("=" * 60)
    
    # Configure for Azure deployment - bind to all interfaces
    os.environ["UVICORN_HOST"] = "0.0.0.0"
    os.environ["UVICORN_PORT"] = "8000"
    
    logger.info(f"Setting UVICORN_HOST to: {os.environ.get('UVICORN_HOST')}")
    logger.info(f"Setting UVICORN_PORT to: {os.environ.get('UVICORN_PORT')}")
    
    # Log environment info
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Working directory: {os.getcwd()}")
    logger.info(f"Environment variables: HOST={os.environ.get('UVICORN_HOST')}, PORT={os.environ.get('UVICORN_PORT')}")
    
    print("Starting Hello World MCP Server with HTTP/SSE transport...")
    print("Server will be available at: http://0.0.0.0:8000")
    print("Server logs will be written to: /tmp/mcp_sse.log")
    print("Test with curl commands from how-to-run-mcp.md")
    print("-" * 50)
    
    logger.info("About to start MCP server with SSE transport")
    
    try:
        # Run with SSE transport - explicitly bind to all interfaces for Azure deployment
        logger.info("Calling mcp.run(transport='sse', host='0.0.0.0', port=8000)")
        mcp.run(transport="sse", host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}", exc_info=True)
        print(f"ERROR: Failed to start server: {e}")
        sys.exit(1)