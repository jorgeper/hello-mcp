#!/usr/bin/env python3
"""
FastMCP Server with basic tools and health resource endpoint.
Uses the mcp.server.fastmcp package for simplified MCP server creation.
"""

import asyncio
import logging
from datetime import datetime
from typing import Any, Dict
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastmcp import FastMCP

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastMCP server instance
mcp = FastMCP("basic-math-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    result = a + b
    logger.info(f"Adding {a} + {b} = {result}")
    return result

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract second number from first number"""
    result = a - b
    logger.info(f"Subtracting {a} - {b} = {result}")
    return result

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together"""
    result = a * b
    logger.info(f"Multiplying {a} * {b} = {result}")
    return result

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide first number by second number"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info(f"Dividing {a} / {b} = {result}")
    return result

@mcp.resource("health://status")
def health_status() -> str:
    """Get the current health status of the server"""
    health_data = {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "server_name": "basic-math-server",
        "version": "1.0.0",
        "uptime": "running",
        "tools_available": ["add", "subtract", "multiply", "divide"],
        "resources_available": ["health://status", "server://info"]
    }
    return str(health_data)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    """Basic health check that the server is running."""
    return JSONResponse({"status": "alive"}, status_code=200)

@mcp.resource("server://info")
def server_info() -> str:
    """Get detailed server information"""
    info_data = {
        "name": "basic-math-server",
        "description": "A FastMCP server providing basic mathematical operations",
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "capabilities": {
            "tools": 4,
            "resources": 2,
            "prompts": 0
        },
        "endpoints": {
            "tools": ["add", "subtract", "multiply", "divide"],
            "resources": ["health://status", "server://info"]
        }
    }
    return str(info_data)

if __name__ == "__main__":
    import uvicorn
    
    # Configure for SSE mode
    logger.info("Starting FastMCP server in SSE mode on http://0.0.0.0:8080")
    
    # Get the FastAPI app and run with uvicorn directly
    try:
        # uvicorn.run(app, 
        mcp.run(transport="sse", host="0.0.0.0", port=8080)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        # Fallback to mcp.run() method