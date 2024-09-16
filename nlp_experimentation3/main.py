# main.py

# technologies/main.py
from factory.named_entity_recognition import NERFactory

def main():
    text = "Hugging Face Inc. is a company based in New York. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge."
    
   # tech = "transformers"  # or "spacy"
    tech = "spacy"  # or "transfomers"
    ner = NERFactory.get_ner_technology(tech)
    
    entities = ner.extract_entities(text)
    for entity, label in entities:
        print(f"Entity: {entity}, Label: {label}")

if __name__ == "__main__":
    main()
