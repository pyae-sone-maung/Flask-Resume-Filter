import os
from typing import Union
from src.app.ai_engine.models.abstract_model import AbstractTextModel, AbstractImageModel
from src.app.ai_engine.models.gemini_model import GeminiModel
from src.app.ai_engine.models.openai_model import OpenAIModel

class AIModelFactory:
    @staticmethod
    def get_model(model_name) -> Union['AbstractTextModel', 'AbstractImageModel']:
        model_name = model_name.lower()
        api_key = f"{model_name.upper()}_API_KEY"
        api_key = os.getenv(api_key)
        
        if not api_key:
            raise ValueError(f"API key for {model_name} not found in environment variables.")

        if model_name == "gemini":
            return GeminiModel(api_key)
        elif model_name == "openai":
            return OpenAIModel(api_key)
        else:
            raise ValueError(f"Unsupported model: {model_name}")