#!/usr/bin/env python3
"""
A simple Hello World MCP server demonstrating basic tool functionality.
"""

import logging
from fastmcp import FastMCP
from datetime import datetime
from typing import Dict, List, Any

# Set up logging for the MCP server
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize the MCP server
logger.info("Initializing FastMCP server: hello-world-server v1.0.0")
mcp = FastMCP(
    "hello-world-server",
)
logger.info("FastMCP server initialized successfully")

@mcp.tool()
def say_hello(name: str = "World") -> str:
    """
    A simple tool that says hello to someone.
    
    Args:
        name: The name to greet (defaults to "World")
        
    Returns:
        A greeting message
    """
    logger.info(f"say_hello called with name: {name}")
    result = f"Hello, {name}! Welcome to MCP!"
    logger.info(f"say_hello returning: {result}")
    return result

@mcp.tool()
def get_greeting_info() -> Dict[str, Any]:
    """
    Returns information about the greeting service.
    
    Returns:
        A dictionary containing service information
    """
    logger.info("get_greeting_info called")
    result = {
        "service": "Hello World MCP Server",
        "version": "1.0.0",
        "current_time": datetime.now().isoformat(),
        "available_languages": ["English"],
        "total_greetings_available": 1
    }
    logger.info(f"get_greeting_info returning: {result}")
    return result

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
    logger.info(f"create_custom_greeting called with name={name}, greeting_type={greeting_type}, include_time={include_time}")
    
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
    
    result = {
        "greeting": greeting,
        "recipient": name,
        "type": greeting_type,
        "timestamp": datetime.now().isoformat() if include_time else None
    }
    logger.info(f"create_custom_greeting returning: {result}")
    return result

@mcp.tool()
def list_available_greetings() -> List[str]:
    """
    Lists all available greeting types.
    
    Returns:
        A list of available greeting types
    """
    logger.info("list_available_greetings called")
    result = ["friendly", "formal", "casual"]
    logger.info(f"list_available_greetings returning: {result}")
    return result

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
    logger.info(f"get_greeting_template called with greeting_type: {greeting_type}")
    
    templates = {
        "friendly": "Hey there, {name}! Great to see you!",
        "formal": "Good day, {name}. How may I assist you?",
        "casual": "What's up, {name}!"
    }
    
    template = templates.get(greeting_type, "Hello, {name}!")
    result = f"Template for {greeting_type}: {template}"
    logger.info(f"get_greeting_template returning: {result}")
    return result

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
    logger.info(f"greeting_prompt called with context: {context}")
    
    base_prompt = "You are a friendly greeting assistant. Generate a warm, welcoming greeting."
    if context:
        base_prompt += f" Context: {context}"
    
    logger.info(f"greeting_prompt returning: {base_prompt}")
    return base_prompt

if __name__ == "__main__":
    # Run the server using stdio transport by default
    import sys
    logger.info("Running MCP server with stdio transport (main entry point)")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Error running MCP server: {e}", exc_info=True)