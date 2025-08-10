import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import Tool

load_dotenv()

API_KEY = os.getenv("API_KEY")


llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=API_KEY,
    model_name="mistralai/mistral-7b-instruct:free",
    temperature=0.7,
)


calculator_tool = PythonREPLTool()

def preprocess_calc_input(text: str) -> str:
    """Remove common calculation keywords and clean the expression."""
    text = text.lower()
    for phrase in ["calculate", "what is", "solve", "evaluate"]:
        text = text.replace(phrase, "")
   
    return text.strip()

def is_calculation_query(text: str) -> bool:
    calc_keywords = ["calculate", "what is", "solve", "+", "-", "*", "/", "=", "evaluate"]
    return any(kw in text.lower() for kw in calc_keywords)

def route_query(query: str) -> str:
    if is_calculation_query(query):
        return "calc"
    return "llm"

st.title("DAG Workflow: Calculator + Mistral LLM ")

user_input = st.text_area("Enter your query:", height=120)

if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter some text")
    else:
        route = route_query(user_input)
        if route == "calc":
            try:
                expression = preprocess_calc_input(user_input)
                
                if not expression.startswith("print("):
                    expression = f"print({expression})"
                output = calculator_tool.run(expression)
                st.markdown("### Calculator output:")
                st.write(output)
            except Exception as e:
                st.error(f"Calculation error: {e}")
        else:
            try:
                response = llm.predict(user_input)
                st.markdown("### LLM output:")
                st.write(response)
            except Exception as e:
                st.error(f"LLM error: {e}")
