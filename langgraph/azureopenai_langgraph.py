import os
import streamlit as st
from dotenv import load_dotenv
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from openai import AzureOpenAI
from langchain_core.messages import AIMessage


load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("API_VERSION", "2025-01-01-preview")  # default if not in .env


client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version,
)


def chatbot_node(state: MessagesState):
    """Convert LangGraph messages to Azure API format and call GPT model."""
    role_map = {
        "human": "user",
        "ai": "assistant",
        "assistant": "assistant",
        "user": "user",
        "system": "system",
        "function": "function"
    }

    formatted_messages = []
    for msg in state["messages"]:
        if isinstance(msg, dict):
            formatted_messages.append({
                "role": role_map.get(msg["role"], msg["role"]),
                "content": msg["content"]
            })
        else:  
            formatted_messages.append({
                "role": role_map.get(msg.type, msg.type),
                "content": msg.content
            })

    response = client.chat.completions.create(
        model=deployment,
        messages=formatted_messages,
        temperature=0.7,
        max_tokens=800
    )

  
    return {"messages": [AIMessage(content=response.choices[0].message.content)]}


memory = MemorySaver()


graph_builder = StateGraph(MessagesState)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile(checkpointer=memory)

#  Streamlit UI
st.set_page_config(page_title="LangGraph Azure Chatbot", page_icon="🤖")
st.title("💬 LangGraph Chatbot with Azure GPT-3.5")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user1"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    result = graph.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config
    )
   
    assistant_msg = result["messages"][-1].content
    st.session_state.chat_history.append(("assistant", assistant_msg))


for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)
