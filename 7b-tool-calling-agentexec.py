from http.client import responses

from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from commons import init_model

@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a+b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a*b

tools = [add, multiply]
llm = init_model()

# Create a prompt template.
# create_tool_calling_agent expects it, and wants {agent_scratchpad} included.
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)

tools_llm = create_tool_calling_agent(llm, tools, prompt_template)
executor = AgentExecutor(agent=tools_llm, tools=tools)

query = input("Ask your question: ")
response =executor.invoke({"input":query})

print(response)