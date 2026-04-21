from streamed_chat import StreamedChat

if __name__ == "__main__":
    chat = StreamedChat(response_format="bash")
    chat.add_user_message(content="Genrate three simple AWS CLI commands. They should be very short")
    chat.get_assistant_response()