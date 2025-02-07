import gradio as gr
from langchain.schema import AIMessage, HumanMessage
from structured_retrieve import run_structured_qa

import commons

model = commons.init_model()

def send_message(message, history):
    history_langchain_format = []
    for msg in history:
        if msg['role'] == "user":
            history_langchain_format.append(HumanMessage(content=msg['content']))
        elif msg['role'] == "assistant":
            history_langchain_format.append(AIMessage(content=msg['content']))

    result = run_structured_qa(message)

    response = f"Summary: {result.summary}\n\nKey Points:\n"
    for kp in result.key_points:
        response += f"- {kp}\n"
    response += f"\nConsider asking: {result.follow_up_question}"

    return response
demo = gr.ChatInterface(
    send_message,
    type="messages"
)

demo.launch()
