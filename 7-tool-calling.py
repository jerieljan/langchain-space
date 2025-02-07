from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool

from commons import init_model


@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a+b

@tool
def multiply(a: int, b: int) -> int:
    """Adds a and b."""
    return a*b

tools = [add, multiply]
model = init_model().bind_tools(tools)

query = input("Ask your question: ")
messages = [HumanMessage(query)]

response = model.invoke(messages)

print(response.pretty_print())
messages.append(response)

for tool_call in response.tool_calls:
    selected_tool = {'add': add, 'multiply': multiply}[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
    print(tool_msg.pretty_print())
    messages.append(tool_msg)

another_response = model.invoke(messages)
print(another_response.pretty_print())
