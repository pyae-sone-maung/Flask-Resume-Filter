from openai import OpenAI
from src.app.ai_engine.prompt_template import RESUME_EXTRACTION_PROMPT
from src.app.ai_engine.models.abstract_model import AbstractTextModel, AbstractImageModel

class OpenAIModel(AbstractTextModel, AbstractImageModel):
    def __init__(self, api_key):
        self.api_key = api_key
        self.prompt_template = RESUME_EXTRACTION_PROMPT
        
    def generate_text(self, prompt, **kwargs):
        pass
    
    def generate_image(self, prompt, **kwargs):
        pass