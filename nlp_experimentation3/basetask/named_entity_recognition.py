# named_entity_recognition.py

from abc import ABC, abstractmethod

class NERBase(ABC):
    @abstractmethod
    def extract_entities(self, text: str):
        pass


