# Simple Rule-Based Chatbot

def chatbot():
    print("ChatBot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == 'bye':
            print("ChatBot: Goodbye! 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm running fine! 😊")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot 1.0, your virtual assistant.")
        elif "help" in user_input:
            print("ChatBot: Sure! Ask me anything about weather, time, or a fun fact.")
        else:
            print("ChatBot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()
