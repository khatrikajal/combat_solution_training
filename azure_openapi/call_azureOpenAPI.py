import os
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "https://azure-apoenai-langgraph.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

if subscription_key is None:
    raise ValueError("AZURE_OPENAI_API_KEY not set in environment")


client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Prepare the chat prompt
chat_prompt = [
    {
        "role": "user",
        "content": "hi"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
    }
]

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=chat_prompt,
    max_tokens=1600,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())
