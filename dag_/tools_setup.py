import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import Tool

load_dotenv()

API_KEY = os.getenv("API_KEY")  

# LLM using your working OpenRouter setup
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=API_KEY,
    model_name="mistralai/mistral-7b-instruct:free",
    temperature=0.7
)

# Calculator tool using Python REPL from experimental package
calculator_tool = PythonREPLTool()

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool.run,
        description="Useful for math calculations",
    ),
]
