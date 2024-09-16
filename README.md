# **NLP Experimentation**

This project contains code and experiments for working with Natural Language Processing (NLP) tools, including SpaCy models and other dependencies managed by Poetry.


## **Requirements**

Before you start, ensure that you have the following installed:

- **Python**: Version 3.10 or higher.
- **Poetry**: For dependency management.

## **Setup Instructions**

Run the setup script
```bash
./setup.sh
```

This will install all necessary dependencies using Poetry and download the SpaCy model (en_core_web_sm)

## **Running the Project**

To run a Python script within Poetry's virtual environment, use
```bash
poetry run python yourscript.py
```

## **Environment Setup**

To run the project with OpenAI API Integration, create a .env file at the root project directory and add your OPENAI API key
```bash
OPENAI_API_KEY=your-key
```
Make sure you gitignore the .env file.