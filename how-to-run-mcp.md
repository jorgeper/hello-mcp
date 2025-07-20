# How to Run and Test the Hello World MCP Server

This guide explains how to run and test your Model Context Protocol (MCP) server locally, including how to connect it to Claude Desktop or test it independently.

## Table of Contents
1. [What is MCP?](#what-is-mcp)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Server](#running-the-server)
5. [Testing Methods](#testing-methods)
6. [Connecting to Claude Desktop](#connecting-to-claude-desktop)
7. [Troubleshooting](#troubleshooting)

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. Think of it like a USB port for AI - it provides a standard way for AI models to connect with external tools and data sources.

MCP servers can expose:
- **Tools**: Functions that the AI can call to perform actions
- **Resources**: Data that can be loaded into the AI's context
- **Prompts**: Reusable templates for AI interactions

## Supported Clients

MCP servers can be used with:
- **Claude Desktop** - Anthropic's desktop application
- **Cursor IDE** - AI-powered code editor with built-in MCP support
- **Custom clients** - Any application that implements the MCP protocol

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Claude Desktop app (for integration testing)

## Installation

1. **Clone or navigate to your project directory:**
   ```bash
   cd hello-mcp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

### Method 1: Direct Python Execution (Recommended for Testing)

The simplest way to run the server is directly with Python:

```bash
python hello_server.py
```

This will start the server in stdio mode. Note that:
- The server communicates via standard input/output
- You'll need an MCP client to interact with it
- The server will wait for client connections

### Method 2: Using the Test Script

To verify the server's tools work correctly without needing a client:

```bash
python test_server.py
```

This will test all the tools and display their outputs.

## Testing Methods

### 1. Using the Test Script (Simplest Method)

The included test script allows you to verify all tools work correctly:

```bash
python test_server.py
```

This will:
- Test each tool with different parameters
- Display the results
- Verify the server configuration
- No client needed for basic testing

### 2. Testing with HTTP API and curl

For easy HTTP testing with curl, use the API wrapper:

```bash
python run_api.py
```

This starts a FastAPI server that wraps the MCP tools. You can then test with curl:

```bash
# List all available tools
curl http://localhost:8000/tools

# Call the say_hello tool
curl -X POST http://localhost:8000/tools/call \
  -H "Content-Type: application/json" \
  -d '{"name": "say_hello", "arguments": {"name": "Alice"}}'

# Call get_greeting_info
curl -X POST http://localhost:8000/tools/call \
  -H "Content-Type: application/json" \
  -d '{"name": "get_greeting_info"}'

# Call create_custom_greeting
curl -X POST http://localhost:8000/tools/call \
  -H "Content-Type: application/json" \
  -d '{
    "name": "create_custom_greeting",
    "arguments": {
      "name": "Bob",
      "greeting_type": "formal",
      "include_time": true
    }
  }'

# List available greeting types
curl -X POST http://localhost:8000/tools/call \
  -H "Content-Type: application/json" \
  -d '{"name": "list_available_greetings"}'
```

You can also visit http://localhost:8000/docs for interactive API documentation.

### 3. Testing with SSE Transport (Advanced)

SSE (Server-Sent Events) transport is designed for persistent connections with MCP clients:

```bash
python run_http.py
```

This runs the actual MCP server with SSE transport. Note that SSE requires a proper MCP client that understands the session-based protocol - it's not designed for simple curl testing.

### 4. Using Cursor IDE

Cursor has built-in MCP support. To use this server with Cursor:

1. **Open Cursor Settings**:
   - Press `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux)
   - Search for "MCP" in settings

2. **Configure MCP Server**:
   - Add a new MCP server configuration
   - Set the command to: `python`
   - Set arguments to: `["/absolute/path/to/hello-mcp/hello_server.py"]`
   - Set the working directory to your project path

3. **Alternative: Edit Cursor Config Directly**:
   
   Find your Cursor config file:
   - Mac: `~/Library/Application Support/Cursor/User/settings.json`
   - Windows: `%APPDATA%\Cursor\User\settings.json`
   - Linux: `~/.config/Cursor/User/settings.json`

   Add this configuration:
   ```json
   {
     "mcpServers": {
       "hello-world": {
         "command": "python",
         "args": ["/Users/jorgepereira/src/hello-mcp/hello_server.py"],
         "cwd": "/Users/jorgepereira/src/hello-mcp",
         "env": {}
       }
     }
   }
   ```

4. **Restart Cursor** and the MCP tools should be available in the AI assistant.

5. **Test in Cursor**:
   - Open a chat with the AI assistant
   - You should see the MCP tools available
   - Try commands like:
     - "Use the say_hello tool to greet me"
     - "What tools are available from the hello-world server?"
     - "Create a formal greeting for Alice with the current time"

### 5. Using Claude Desktop (Full Integration)

The most complete way to test is by connecting to Claude Desktop (see instructions below).

### 6. Testing with a Python Client

Create a test client script (`test_client.py`):

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
import subprocess

async def test_server():
    # Start the server process
    server_params = StdioServerParameters(
        command="python",
        args=["hello_server.py"],
        env=None
    )
    
    async with ClientSession(server_params) as session:
        # Initialize the connection
        await session.initialize()
        
        # List available tools
        tools = await session.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        
        # Call the say_hello tool
        result = await session.call_tool("say_hello", {"name": "Test User"})
        print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(test_server())
```

## Connecting to Claude Desktop

### Step 1: Manual Configuration

Since the MCP package doesn't include a CLI installer, you'll need to manually configure Claude Desktop:

1. **Find the config file:**
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **Add your server configuration:**
   ```json
   {
     "mcpServers": {
       "hello-world": {
         "command": "python",
         "args": ["/absolute/path/to/hello_server.py"],
         "env": {
           "PYTHONPATH": "/absolute/path/to/hello-mcp"
         }
       }
     }
   }
   ```

3. **Restart Claude Desktop** for changes to take effect.

### Step 2: Verify Connection

1. Open Claude Desktop
2. Start a new conversation
3. Look for the MCP tools icon (usually a puzzle piece or tool icon)
4. You should see your tools listed:
   - `say_hello`
   - `get_greeting_info`
   - `create_custom_greeting`
   - `list_available_greetings`

### Step 3: Test the Tools

Try these prompts in Claude Desktop:
- "Use the say_hello tool to greet me"
- "What greeting types are available?"
- "Create a formal greeting for Alice with the current time"

## Server Capabilities

Our hello-world server provides:

### Tools:
1. **say_hello**: Basic greeting function
2. **get_greeting_info**: Returns server information
3. **create_custom_greeting**: Advanced greeting with options
4. **list_available_greetings**: Shows greeting types

### Resources:
- `greeting://template/{type}`: Greeting templates

### Prompts:
- `greeting_prompt`: Template for generating greetings

## Testing Methods Summary

| Method | Command | Use Case |
|--------|---------|----------|
| Direct Test | `python test_server.py` | Quick verification of tools |
| HTTP API | `python run_api.py` + curl | REST API testing, debugging |
| SSE Transport | `python run_http.py` | MCP web clients |
| stdio | `python hello_server.py` | Claude Desktop, Cursor IDE |
| Python Client | Custom script | Advanced testing |

## Troubleshooting

### Common Issues:

1. **"Module not found" error:**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: `pip install -r requirements.txt`

2. **Claude Desktop doesn't show tools:**
   - Check the config file path is correct
   - Ensure Python path in config is absolute
   - Restart Claude Desktop
   - Check Claude Desktop logs for errors

3. **Server won't start:**
   - Check Python version: `python --version` (needs 3.8+)
   - Verify file permissions: `chmod +x hello_server.py`
   - Check for port conflicts if using development mode

4. **Tools fail to execute:**
   - Check server logs for error messages
   - Verify parameter types match the function signatures
   - Test tools individually using the MCP CLI

### Debugging Tips:

1. **Enable verbose logging:**
   ```bash
   MCP_LOG_LEVEL=DEBUG python hello_server.py
   ```

2. **Check Claude Desktop logs:**
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%LOCALAPPDATA%\Claude\Logs\`

3. **Test with the inspector:**
   ```bash
   mcp-inspector hello_server.py --verbose
   ```

## Next Steps

Once you have the basic server working:

1. **Add more tools**: Implement additional functionality
2. **Add resources**: Expose data through the resource system
3. **Create prompts**: Build reusable prompt templates
4. **Handle errors**: Add proper error handling and validation
5. **Add persistence**: Store state between calls if needed
6. **Implement streaming**: For long-running operations

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Awesome List](https://github.com/modelcontextprotocol/awesome-mcp)
- [Community Servers](https://github.com/modelcontextprotocol/servers)

## Support

If you encounter issues:
1. Check the [MCP Python SDK issues](https://github.com/modelcontextprotocol/python-sdk/issues)
2. Join the MCP community discussions
3. Review the server logs for detailed error messages