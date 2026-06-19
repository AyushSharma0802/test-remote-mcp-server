from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator Server")

@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """
    Adds two numbers together and returns the sum.

    Args:
        a: The first number to add.
        b: The second number to add.
    """
    total = a + b
    return f"The sum of {a} and {b} is {total}."

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port= 8000)
