import asyncio

from src.agent import Agent
from src.tools import tools, tool_descriptions

def main():
    instructions= (
        "You are a tool calling agent that may use the following tools by responding according to their instructions. \n"
        "Available tools:\n"
        f"{tool_descriptions}\n"
        "If not tool is needed, respons with the final answer."
    )

    agent = Agent(
        tools=tools,
        instructions=instructions
    )

    #run loop
    print("Hello! You are now chatting with you Agent.")
    print("Type 'exit' or 'quit' or 'bye' to end the chat")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {'exit', 'quit', 'bye'}:
            print("Goodbye")
            break
        result = asyncio.run(agent.run(user_input=user_input))
        print(f"Agent: {result.strip()}")

if __name__ == "__main__":
    main()
