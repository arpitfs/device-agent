import re

from src.model import ModelInterface
from src.tools import Tool

class Agent:
    def __init__(
        self,
        tools: list[Tool],
        instructions: str
    ):
       #model used by agent
       self.model = ModelInterface()

       #tools available  as functions to the agent 
       self.tools = {tool.name: tool for tool in tools}

       # agent instructions to set behaviour

       self.instructions = instructions

    async def run(
        self,
        user_input: str      
    ):
        history = [
            {
                "role": "system",
                "content": self.instructions
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
        # looks for tool calls in the : Funcion() where Function is replaced by the tool name
        tool_call_pattern = re.compile(r"^(\w+)\((.*)\)", re.DOTALL)

        #call the model
        response = self.model.chatcompletion(history)

        #check  the output for a tool match
        match = tool_call_pattern.match(response.strip())

        if match:
            name, arg = match.groups()
            tool = self.tools.get(name)
            if tool:
                #check for arguments
                result = tool.run(arg) if arg else tool.run("")
                history.append(
                    {
                        "role": "assistant",
                        "content": response.strip()
                    }
                )
                history.append(
                    {
                        "role": "tool",
                        "content": result
                    }
                )       
                return result.strip()         

        else:
            history.append(
                {
                    "role": "assistant",
                    "content": response.strip()
                }
            )
            return response.strip()