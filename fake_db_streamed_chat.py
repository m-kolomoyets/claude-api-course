from streamed_chat import StreamedChat

if __name__ == "__main__":
    chat = StreamedChat()
    chat.add_user_message("Write a definition of fake database. 1-2 sentences")
    chat.get_assistant_response()