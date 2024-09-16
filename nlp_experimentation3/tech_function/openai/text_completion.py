



import os
import sys


# Set up the environment and path settings
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from basetask.text_completion import TextCompletionBase
from basetechnology.openai import OpenAIBase

class OpenAITextCompletion(TextCompletionBase, OpenAIBase):
    def __init__(self):
        super().__init__()  # Initialize OpenAIBase to handle API key

    def complete_text(self, prompt: str, model="gpt-4", max_tokens=150, temperature=0):
        """
        Generate text completion using OpenAI API.
        
        Parameters:
            prompt (str): The prompt to be completed.
            model (str): The model to use for completion (default: gpt-4).
            max_tokens (int): Maximum number of tokens to generate (default: 150).
            temperature (float): Sampling temperature for the model (default: 0).

        Returns:
            str: The generated text completion.
        """
        messages = [{"role": "user", "content": prompt}]
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            completion_text = response.choices[0].message.content
            return completion_text
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return str(e)

   

# Example usage
if __name__ == "__main__":
    text_completion = OpenAITextCompletion()
    
    # Example text completion
    result = text_completion.complete_text("Once upon a time,")
    print("Text Completion Result:", result)
    
