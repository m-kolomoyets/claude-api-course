from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"

def print_user_message(content):
    print(f"\n--- User ---\n{content}\n")


class StreamedChat:
    def __init__(self, system_prompt="", model=model):
        self.model = model
        self.client = Anthropic()
        self.messages = []
        self.system_prompt = system_prompt
    
    def add_user_message(self, content):
        print_user_message(content)
        self.messages.append({"role": "user", "content": content})
        return content
    
    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})
        return content
    
    def get_assistant_response(self):
        with self.client.messages.stream(model=self.model, max_tokens=1000, messages=self.messages, system=self.system_prompt) as stream:
            print(f"\n--- Assistant ---\n")
            for text in stream.text_stream:
                print(text, end="")
            final_response = stream.get_final_message()
            self.add_assistant_message(final_response.content[0].text)
        return final_response

        
    
    def get_messages(self):
        return self.messages
