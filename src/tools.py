from datetime import datetime

class Tool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description

    def run(self, arg):
        return self.func(arg) if arg != "" else self.func()


def time_tool():
    """Tell the current time"""
    now = datetime.now()
    return f"The current time  is {now.strftime('%I:%M%p').lstrip('0').lower()} on {now.strftime('%d %B %Y')}"

tools = [
    Tool(
        "Time",
        time_tool,
        "Prints the current date and time. Usage: return 'Time()'"
    )
]

#describes  the tools  for the system prompt
tool_descriptions = "\n".join(
    f"- {tool.name}: {tool.description}" for tool in tools
)