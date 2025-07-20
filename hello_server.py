#!/usr/bin/env python3
"""
A simple Hello World MCP server demonstrating basic tool functionality.
"""

from mcp.server.fastmcp import FastMCP
from datetime import datetime
from typing import Dict, List, Any

# Initialize the MCP server
mcp = FastMCP(
    "hello-world-server",
    version="1.0.0",
    description="A simple MCP server that demonstrates basic functionality"
)

@mcp.tool()
def say_hello(name: str = "World") -> str:
    """
    A simple tool that says hello to someone.
    
    Args:
        name: The name to greet (defaults to "World")
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to MCP!"

@mcp.tool()
def get_greeting_info() -> Dict[str, Any]:
    """
    Returns information about the greeting service.
    
    Returns:
        A dictionary containing service information
    """
    return {
        "service": "Hello World MCP Server",
        "version": "1.0.0",
        "current_time": datetime.now().isoformat(),
        "available_languages": ["English"],
        "total_greetings_available": 1
    }

@mcp.tool()
def create_custom_greeting(
    name: str,
    greeting_type: str = "friendly",
    include_time: bool = False
) -> Dict[str, str]:
    """
    Creates a custom greeting with various options.
    
    Args:
        name: The name to include in the greeting
        greeting_type: Type of greeting - "friendly", "formal", or "casual"
        include_time: Whether to include the current time in the greeting
        
    Returns:
        A dictionary with the greeting and metadata
    """
    greetings = {
        "friendly": f"Hey there, {name}! Great to see you!",
        "formal": f"Good day, {name}. How may I assist you?",
        "casual": f"What's up, {name}!"
    }
    
    greeting = greetings.get(greeting_type, greetings["friendly"])
    
    if include_time:
        current_hour = datetime.now().hour
        time_greeting = "Good morning" if current_hour < 12 else "Good afternoon" if current_hour < 18 else "Good evening"
        greeting = f"{time_greeting}, {name}! {greeting}"
    
    return {
        "greeting": greeting,
        "recipient": name,
        "type": greeting_type,
        "timestamp": datetime.now().isoformat() if include_time else None
    }

@mcp.tool()
def list_available_greetings() -> List[str]:
    """
    Lists all available greeting types.
    
    Returns:
        A list of available greeting types
    """
    return ["friendly", "formal", "casual"]

# Resource example - provides static or dynamic content
@mcp.resource("greeting://template/{greeting_type}")
def get_greeting_template(greeting_type: str) -> str:
    """
    Returns a greeting template for the specified type.
    
    Args:
        greeting_type: The type of greeting template to return
        
    Returns:
        A template string for the greeting
    """
    templates = {
        "friendly": "Hey there, {name}! Great to see you!",
        "formal": "Good day, {name}. How may I assist you?",
        "casual": "What's up, {name}!"
    }
    
    template = templates.get(greeting_type, "Hello, {name}!")
    return f"Template for {greeting_type}: {template}"

# Prompt example - provides reusable prompt templates
@mcp.prompt()
def greeting_prompt(context: str = "") -> str:
    """
    A prompt template for generating greetings.
    
    Args:
        context: Additional context for the greeting
        
    Returns:
        A prompt template
    """
    base_prompt = "You are a friendly greeting assistant. Generate a warm, welcoming greeting."
    if context:
        base_prompt += f" Context: {context}"
    return base_prompt

if __name__ == "__main__":
    # Run the server using stdio transport by default
    import sys
    mcp.run(transport="stdio")