from abc import ABC, abstractmethod

class AbstractTextModel(ABC):
    @abstractmethod
    def generate_text(self, prompt, **kwargs):
        pass
    
class AbstractImageModel(ABC):
    @abstractmethod
    def generate_image(self, prompt, **kwargs):
        pass