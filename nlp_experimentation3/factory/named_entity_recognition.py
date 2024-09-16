# named_entity_recognition.py

# technologies/ner_factory.py
from basetask.named_entity_recognition import NERBase
from tech_function.spacy.named_entity_recognition import SpacyNER
from tech_function.huggingface.named_entity_recognition import TransformersNER

class NERFactory:
    @staticmethod
    def get_ner_technology(tech: str) -> NERBase:
        if tech == "spacy":
            return SpacyNER()
        elif tech == "transformers":
            
            return TransformersNER()
        else:
            raise ValueError(f"Unknown technology: {tech}")
