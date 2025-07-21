import google.generativeai as genai
from google.generativeai import types

from src.app.ai_engine.prompt_template import RESUME_EXTRACTION_PROMPT
from src.app.ai_engine.models.abstract_model import AbstractTextModel

class GeminiModel(AbstractTextModel):
    def __init__(self, api_key):
        self.api_key = api_key
        self.prompt_template = RESUME_EXTRACTION_PROMPT
        
    def generate_text(self, prompt, **kwargs):
        response_text = ""
        prompt = self.prompt_template.format(resume_text=prompt)
        
        client = genai.GenerativeModel("gemini-2.5-flash")
        genai.configure(api_key=self.api_key)
        config = types.GenerationConfig(
            temperature=0.3
        )
        
        response = client.generate_content(
            contents = prompt,
            generation_config = config
        )
        
        if response.candidates:
            first_candidate = response.candidates[0]
            if first_candidate.content and first_candidate.content.parts:
                json_text = first_candidate.content.parts[0].text
                response_text = json_text.strip('```json\n').strip('```').strip()
        return response_text

