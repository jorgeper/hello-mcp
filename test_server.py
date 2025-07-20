#!/usr/bin/env python3
"""
Simple test script to verify the MCP server functionality.
"""

from hello_server import mcp, say_hello, get_greeting_info, create_custom_greeting, list_available_greetings

def test_tools():
    """Test all the tools without running the server."""
    
    print("Testing MCP Server Tools\n" + "="*30)
    
    # Test say_hello
    print("\n1. Testing say_hello():")
    print(f"   Default: {say_hello()}")
    print(f"   With name: {say_hello('Alice')}")
    
    # Test get_greeting_info
    print("\n2. Testing get_greeting_info():")
    info = get_greeting_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Test create_custom_greeting
    print("\n3. Testing create_custom_greeting():")
    greetings = [
        ("Bob", "friendly", False),
        ("Carol", "formal", True),
        ("Dave", "casual", False)
    ]
    for name, greeting_type, include_time in greetings:
        result = create_custom_greeting(name, greeting_type, include_time)
        print(f"   {greeting_type} greeting for {name}:")
        print(f"     {result['greeting']}")
    
    # Test list_available_greetings
    print("\n4. Testing list_available_greetings():")
    available = list_available_greetings()
    print(f"   Available types: {', '.join(available)}")
    
    # Test server info
    print("\n5. Server Information:")
    print(f"   Name: {mcp.name}")
    print(f"   Number of tools: {len(mcp._tool_manager._tools)}")
    
    print("\n" + "="*30)
    print("All tests completed successfully!")

if __name__ == "__main__":
    test_tools()