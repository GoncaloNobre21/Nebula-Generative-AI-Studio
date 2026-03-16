import os
from typing import Any, Dict, List
import openai
from anthropic import Anthropic
from transformers import pipeline

class LLMManager:
    """
    Manages multiple LLM providers, providing a unified interface for text generation.
    """
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    def generate_openai(self, prompt: str, model: str = "gpt-4") -> str:
        """Generates text using OpenAI's GPT-4 model."""
        client = openai.OpenAI(api_key=self.openai_api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def generate_anthropic(self, prompt: str, model: str = "claude-3-opus-20240229") -> str:
        """Generates text using Anthropic's Claude 3 Opus model."""
        client = Anthropic(api_key=self.anthropic_api_key)
        message = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    def generate_hf(self, prompt: str, model_name: str = "gpt2") -> str:
        """Generates text using a HuggingFace pipeline."""
        generator = pipeline("text-generation", model=model_name)
        return generator(prompt, max_length=50)[0]['generated_text']
