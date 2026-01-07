from fastmcp import FastMCP
import random
import json

mcp = FastMCP('Simple Calculator Server')

# tool: add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """ Add two numbers """
    return a+b

# tool: generate a random number
@mcp.tool
def random_number_generator(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number within a range. """
    return random.randint(min_val, max_val)

# resource: server information
@mcp.resource('info://server')
def server_info() -> str:
    """ Get information about this server. """
    infor = {
        "name": "Simple Calculator server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "coder"
    }
    return json.dumps(info, indent=2)



if __name__ == "__main__":
    # in local
    # mcp.run() - default, making it run on same machine
    mcp.run(transport="http", host='0.0.0.0', port=8000)
