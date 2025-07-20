#!/usr/bin/env python3
"""
HTTP API server for testing MCP tools with curl.
This creates a simple FastAPI wrapper around the MCP tools.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, Optional
import uvicorn

from hello_server import (
    say_hello, 
    get_greeting_info, 
    create_custom_greeting, 
    list_available_greetings
)

app = FastAPI(title="Hello MCP API", version="1.0.0")

class ToolCallRequest(BaseModel):
    name: str
    arguments: Optional[Dict[str, Any]] = {}

@app.get("/")
def root():
    return {"message": "Hello MCP API Server", "endpoints": ["/tools", "/tools/call"]}

@app.get("/tools")
def list_tools():
    """List all available tools"""
    return {
        "tools": [
            {
                "name": "say_hello",
                "description": "A simple tool that says hello to someone",
                "parameters": {"name": "string (optional, default='World')"}
            },
            {
                "name": "get_greeting_info",
                "description": "Returns information about the greeting service",
                "parameters": {}
            },
            {
                "name": "create_custom_greeting",
                "description": "Creates a custom greeting with various options",
                "parameters": {
                    "name": "string (required)",
                    "greeting_type": "string (optional, default='friendly')",
                    "include_time": "boolean (optional, default=False)"
                }
            },
            {
                "name": "list_available_greetings",
                "description": "Lists all available greeting types",
                "parameters": {}
            }
        ]
    }

@app.post("/tools/call")
def call_tool(request: ToolCallRequest):
    """Call a specific tool with arguments"""
    tool_map = {
        "say_hello": say_hello,
        "get_greeting_info": get_greeting_info,
        "create_custom_greeting": create_custom_greeting,
        "list_available_greetings": list_available_greetings
    }
    
    if request.name not in tool_map:
        return JSONResponse(
            status_code=404,
            content={"error": f"Tool '{request.name}' not found"}
        )
    
    try:
        tool = tool_map[request.name]
        result = tool(**request.arguments)
        return {
            "tool": request.name,
            "result": result
        }
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    print("Starting Hello MCP API Server...")
    print("Server will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    print("-" * 50)
    print("\nExample curl commands:")
    print("  curl http://localhost:8000/tools")
    print("  curl -X POST http://localhost:8000/tools/call \\")
    print("    -H 'Content-Type: application/json' \\")
    print("    -d '{\"name\": \"say_hello\", \"arguments\": {\"name\": \"World\"}}'")
    print("-" * 50)
    
    uvicorn.run(app, host="0.0.0.0", port=8080)