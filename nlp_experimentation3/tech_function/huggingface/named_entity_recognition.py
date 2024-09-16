# transformers_ner.py
import torch
from transformers import pipeline
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from basetask.named_entity_recognition import NERBase
import transformers


class TransformersNER(NERBase):
    def __init__(self, model_name="dbmdz/bert-large-cased-finetuned-conll03-english", tokenizer_name=None, device=-1):
        """
        Initialize the TransformersNER class with a specified model and tokenizer.
        
        Parameters:
        - model_name (str): The name of the model to use. Default is 'dbmdz/bert-large-cased-finetuned-conll03-english' which is the default in the pipeline in transformers.
        - tokenizer_name (str): The name of the tokenizer to use. If None, uses the model_name. Default is None.
        - device (int): The device to run the model on. Default is -1 (CPU). Use 0 for GPU.
        
        """
        if tokenizer_name is None:
            tokenizer_name = model_name
        
        self.ner_pipeline = pipeline("ner", model=model_name, tokenizer=tokenizer_name, device=device)
    
    def extract_entities(self, text: str):
        """
        Extract entities from the given text using the NER pipeline.
        
        Parameters:
        - text (str): The input text for entity extraction.
        
        Returns:
        - List[Tuple[str, str]]: A list of tuples containing the entity text and its label.
        """
        entities = self.ner_pipeline(text)
        return [(entity['word'], entity['entity']) for entity in entities]

# Example usage
if __name__ == "__main__":
    ner = TransformersNER(model_name="xlm-roberta-large-finetuned-conll03-english", device=-1)
    text = "Hugging Face Inc. is a company based in New York."
    entities = ner.extract_entities(text)
    for entity, label in entities:
        print(f"Entity: {entity}, Label: {label}")
