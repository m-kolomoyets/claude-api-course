from chat import Chat

if __name__ == "__main__":
    chat = Chat()
    chat.add_user_message("What is quantum computing? Answer in one sentence")
    chat.get_assistant_response()
    chat.add_user_message("Write another sentence")
    chat.get_assistant_response()