from flask import current_app
from src.app.ai_engine.core.engine import AIEngine

def retrieve_resume_data(prompt: str, model_name: str):
    ai_engine = AIEngine()
    response = None

    try:
        response = ai_engine.generate_text(prompt, model_name=model_name)
        return response
    except Exception as ex:
        current_app.logger.error(f"Error running ai task: {ex}")
        raise ValueError(f"Error running ai task: {ex}")