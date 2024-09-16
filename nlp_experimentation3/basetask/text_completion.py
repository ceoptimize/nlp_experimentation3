# text_completion.py

from abc import ABC, abstractmethod

class TextCompletionBase(ABC):
    @abstractmethod
    def complete_text(self, prompt: str):
        pass