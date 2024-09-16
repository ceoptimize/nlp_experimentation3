import os
import sys
import json
# Set up the environment and path settings
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from basetask.text_completion import TextCompletionBase
from basetechnology.openai import OpenAIBase

class OpenAITextCompletion(TextCompletionBase, OpenAIBase):
    
    def __init__(self, prompt: str, model="gpt-4", max_tokens=150, temperature=0, tools=None):
        super().__init__()  # Initialize OpenAIBase to handle API key
        self.completion_message = self.getCompletionMessage(prompt, model, max_tokens, temperature, tools)
    

    def getCompletionMessage(self, prompt: str, model="gpt-4", max_tokens=150, temperature=0, tools=None):
        """
        Generate text completion using OpenAI API with function calling support.
        
        Parameters:
            prompt (str): The prompt to be completed.
            model (str): The model to use for completion (default: gpt-4).
            max_tokens (int): Maximum number of tokens to generate (default: 150).
            temperature (float): Sampling temperature for the model (default: 0).
            tools (list): List of function definitions for function calling (default: None).

        Returns:
            str: The generated text completion or function call suggestion.
        """
        messages = [{"role": "user", "content": prompt}]
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                tools=tools  # Pass tools for function calling
            )
            
            result = response.choices[0].message
            self.completion_message = result
            return result
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return str(e)
        
    def complete_text(self):
     #   self.getCompletionMessage(prompt, model, max_tokens, temperature, tools)
        complete_text = self.completion_message.content
        return complete_text
    
  
    def getCompletionToolCalls(self):
        tool_calls = self.completion_message.tool_calls
        if tool_calls:
            tool_call = tool_calls[0]
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            return f"Function Call Suggested: {function_name} with arguments {arguments}"
            
        return None

# Example usage
if __name__ == "__main__":

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_delivery_date",
                "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The customer's order ID.",
                        },
                    },
                    "required": ["order_id"],
                    "additionalProperties": False,
                },
            }
        }
    ]
    text_completion = OpenAITextCompletion("my order number is 12345,", tools = tools)
    #print(text_completion.completion_message)
    
        
    result = text_completion.complete_text()
    print("Text Completion Content:", result)
        
    result = text_completion.getCompletionToolCalls()
    print("Text Completion Tool Calls:", result)