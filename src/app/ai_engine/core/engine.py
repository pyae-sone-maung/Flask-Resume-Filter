from flask import current_app
from src.app.ai_engine.core.factory import AIModelFactory
from src.app.ai_engine.models.abstract_model import AbstractTextModel, AbstractImageModel

class AIEngine:
    def __init__(self):
        self.factory = AIModelFactory
        self._current_model: AbstractTextModel = None
        self._current_model_name: str = None
        self.initialize_model = {}
        
    def set_active_model(self, model_name: str):
        model_name = model_name.lower()
        if self._current_model_name != model_name:
            current_app.logger.info(f"Active model : {model_name}")
            if model_name not in self.initialize_model:
                try:
                    self.initialize_model[model_name] = self.factory.get_model(model_name)
                except Exception as ex:
                    current_app.logger.error(f"Error initializing model {model_name} : {ex}")
                    raise ValueError(f"Error initializing model {model_name} : {ex}")
            self._current_model = self.initialize_model[model_name]
            self._current_model_name = model_name
        else:
            current_app.logger.info(f"Already active model : {model_name}")
            
    def get_active_model(self):
        if self._current_model is None:
            current_app.logger.error("No active model")
            raise ValueError("No active model")
        return self._current_model
    
    def generate_text(self, prompt, model_name, **kwargs):
        if model_name:
            self.set_active_model(model_name)
        model = self.get_active_model()
        try:
            return model.generate_text(prompt, **kwargs)
        except Exception as ex:
            current_app.logger.error(f"Error generating text for model {model_name} : {ex}")
            raise ValueError(f"Error generating text for model {model_name} : {ex}")
    
    def generate_image(self, prompt: str, model_name: str = None, **kwargs):
        if model_name:
            self.set_active_model(model_name)
        model = self.get_active_model()
        return model.generate_image(prompt, **kwargs)

    @staticmethod
    def get_supported_models() -> list[str]:
        return ["gemini", "openai"]