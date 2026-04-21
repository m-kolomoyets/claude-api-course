from chat import Chat

math_system_prompt ="""
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

if __name__ == "__main__":
    chat = Chat(system_prompt=math_system_prompt)
    chat.add_user_message("How do I solve 5x + 2 = 3 for x?")
    chat.get_assistant_response()