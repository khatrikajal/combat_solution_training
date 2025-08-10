import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


load_dotenv()
MODEL = "mistralai/mistral-7b-instruct:free"
API_KEY = os.getenv("API_KEY") 


llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=API_KEY,
    model_name=MODEL,
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
    You are a helpful assistant.
    Conversation so far:
    {history}
    User: {input}
    AI:"""
)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")


if "chain" not in st.session_state:
    st.session_state.chain = LLMChain(llm=llm, prompt=prompt, memory=st.session_state.memory)


st.title("LangChain Chat — Mistral-7B via OpenRouter")
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    try:
        response = st.session_state.chain.run(user_input)
        st.write(f"**Assistant:** {response}")
    except Exception as e:
        st.error(f"Error: {str(e)}")


st.subheader("Conversation History")
history_data = st.session_state.memory.load_memory_variables({})
st.write(history_data.get("history", "No history yet."))

if st.button("Clear Memory"):
    st.session_state.memory.clear()
    st.success("Memory cleared!")
