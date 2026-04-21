from dotenv import load_dotenv
load_dotenv()

from typing import Literal, Optional
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"

ResponseFormat = Optional[Literal["bash", "json"]]

FORMAT_INSTRUCTIONS = {
    "bash": "Respond with a single ```bash fenced code block and nothing else. Do not include any comments (no lines starting with `#`) inside the block.",
    "json": "Respond with a single ```json fenced code block and nothing else. The block must contain valid JSON.",
}


def print_user_message(content):
    print(f"\n--- User ---\n{content}\n")


def strip_bash_comments(text: str) -> str:
    cleaned = []
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("#") and not stripped.startswith("#!"):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


class StreamedChat:
    def __init__(self, system_prompt="", model=model, response_format: ResponseFormat = None):
        self.model = model
        self.client = Anthropic()
        self.messages = []
        self.response_format = response_format
        self.system_prompt = self._build_system_prompt(system_prompt)

    def _build_system_prompt(self, base: str) -> str:
        instruction = FORMAT_INSTRUCTIONS.get(self.response_format) if self.response_format else None
        if not instruction:
            return base
        return f"{base}\n\n{instruction}".strip()

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
            buffer = ""
            for text in stream.text_stream:
                buffer += text
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self._emit(line + "\n")
            if buffer:
                self._emit(buffer)
            final_response = stream.get_final_message()
            content = final_response.content[0].text
            if self.response_format == "bash":
                content = strip_bash_comments(content)
            self.add_assistant_message(content)
        return final_response

    def _emit(self, chunk: str):
        if self.response_format == "bash":
            stripped = chunk.lstrip()
            if stripped.startswith("#") and not stripped.startswith("#!"):
                return
        print(chunk, end="")

    def get_messages(self):
        return self.messages
