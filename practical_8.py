import sys

# rule-based chatbot using pattern matching

RULES = [
    (['hello', 'hi', 'hey'], "Hello! How can I help you?"),
    (['name'], "I am a simple AI chatbot."),
    (['how are you'], "I am fine. Thank you for asking!"),
    (['course', 'subject'], "I can provide basic information about your course."),
    (['help'], "Sure! You can ask me about my name, course, or general information."),
    (['thank', 'thanks'], "You are welcome!"),
]

EXIT_PATTERNS = ['bye', 'exit', 'quit']
DEFAULT_RESPONSE = "Sorry, I do not understand your question."


def get_response(user_input):
    text = user_input.lower().strip()

    # check if user wants to exit
    for pattern in EXIT_PATTERNS:
        if pattern in text:
            return "Goodbye! Have a nice day.", True

    # check predefined pattern rules
    for patterns, response in RULES:
        for pattern in patterns:
            if pattern in text:
                return response, False

    # default response when no pattern matches
    return DEFAULT_RESPONSE, False


def run_chatbot():
    print("Chatbot: Hello! Type 'bye', 'exit', or 'quit' to leave the chat.\n")

    # interactive mode if terminal input is connected
    if sys.stdin.isatty():
        while True:
            try:
                user_msg = input("User: ")
            except (EOFError, KeyboardInterrupt):
                print("\nChatbot: Goodbye! Have a nice day.")
                break

            response, is_exit = get_response(user_msg)
            print(f"Chatbot: {response}")
            if is_exit:
                break
    else:
        # demo run using sample inputs from manual
        sample_inputs = [
            "Hi",
            "What is your name?",
            "Can you help me?",
            "What is the subject?",
            "Good morning",
            "Bye"
        ]
        for msg in sample_inputs:
            print(f"User: {msg}")
            response, is_exit = get_response(msg)
            print(f"Chatbot: {response}")
            if is_exit:
                break


if __name__ == '__main__':
    run_chatbot()
