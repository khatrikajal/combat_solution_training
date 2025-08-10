from langchain.llms.base import LLM
from typing import Optional, List
import httpx
from pydantic import BaseModel

class OpenRouterLLM(LLM):
    api_key: str
    model: str = "mistralai/mistral-7b-instruct:free"
    api_url: str = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, **data):
        super().__init__(**data)

    @property
    def _llm_type(self) -> str:
        return "openrouter"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        
        json_payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 256,
            "temperature": 0.7,
        }

        with httpx.Client(timeout=15) as client:
            response = client.post(self.api_url, headers=headers, json=json_payload)
            response.raise_for_status()
            data = response.json()
            
            return data["choices"][0]["message"]["content"].strip()
