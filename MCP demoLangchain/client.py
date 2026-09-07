from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os
import sys

load_dotenv()

async def main():
    # Use the venv's python executable so the math server runs in the same environment
    python_exe = sys.executable

    client = MultiServerMCPClient(
        {
            "math": {
                "command": python_exe,
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            }
        }
    )

    tools = await client.get_tools()

    model = ChatGroq(model="qwen/qwen3.6-27b", max_tokens=512)
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3+5) x 12?"}]}
    )
    print("Math Response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's the weather in California?"}]}
    )
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())