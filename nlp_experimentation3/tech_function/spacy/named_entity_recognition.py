# named_entity_recognition.py

# spacy_ner.py
import spacy
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from basetask.named_entity_recognition import NERBase
from basetechnology.spacy import SpacyBase


    
class SpacyNER(NERBase, SpacyBase):
    def __init__(self):
        super().__init__()  # Call the constructor of the first parent class
        self.nlp = spacy.load("en_core_web_sm")
    
    def extract_entities(self, text: str):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
