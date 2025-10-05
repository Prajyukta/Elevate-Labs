print("🤖 Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print("🤖 Chatbot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("🤖 Chatbot: I'm a rule-based chatbot built in Python!")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great, thank you! How about you?")

    elif "bye" in user_input:
        print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I didn’t understand that.")
