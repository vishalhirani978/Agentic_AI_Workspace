from httpx import __name
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather (location:str)->str:
    """get the weather of location"""
    return f"The weather in calfornia  is sunny with a high of 75 degrees"

if __name__ == "__main__":
   mcp.run(transport="streamable-http")