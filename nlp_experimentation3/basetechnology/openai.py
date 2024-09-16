from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class OpenAIBase:
    def __init__(self):
        # Load OpenAI API key from environment variables
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables.")
        
     

        self.client = OpenAI(api_key=self.api_key)
        