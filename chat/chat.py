from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"

def print_user_message(content):
    print(f"--- User ---\n{content}\n")

def print_assistant_message(content):
    print(f"--- Assistant ---\n{content}\n")

class Chat:
    def __init__(self, system_prompt="", model=model):
        self.model = model
        self.client = Anthropic()
        self.messages = []
        self.system_prompt = system_prompt
    
    def add_user_message(self, content=""):
        print_user_message(content)
        self.messages.append({"role": "user", "content": content})
        return content
    
    def add_assistant_message(self, content=""):
        print_assistant_message(content)
        self.messages.append({"role": "assistant", "content": content})
        return content
    
    def get_assistant_response(self):
        response = self.client.messages.create(model=self.model, max_tokens=1000, messages=self.messages, system=self.system_prompt)
        response_text = response.content[0].text
        self.add_assistant_message(response_text)
        return response_text
    
    def get_messages(self):
        return self.messages
