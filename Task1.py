import re

def chatbot():
    print("Hello! I am a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if re.search(r"\bhello\b|\bhi\b", user_input):
            response = "Hello! How can I assist you today?"
        elif re.search(r"\bhow are you\b", user_input):
            response = "I'm just a bunch of code, but I'm functioning as expected! How are you?"
        elif re.search(r"\bwhat is your name\b", user_input):
            response = "I am a simple chatbot created to help you with basic queries."
        elif re.search(r"\bhelp\b", user_input):
            response = "Sure, I'm here to help! You can ask me about the weather, time, or general questions."
        elif re.search(r"\bweather\b", user_input):
            response = "I can't provide real-time weather updates yet, but you can check your local weather forecast online."
        elif re.search(r"\btime\b", user_input):
            response = "I don't have a clock, but you can check the time on your device."
        elif re.search(r"\bbye\b|\bexit\b", user_input):
            response = "Goodbye! Have a great day!"
            print("Chatbot: " + response)
            break
        else:
            response = "I'm sorry, I don't understand that. Can you ask something else?"

        print("Chatbot: " + response)

# Run the chatbot
chatbot()
