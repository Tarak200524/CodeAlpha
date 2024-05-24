import random
chat = 1
while chat:
    greetings = ["hi", "hello", "hey"]
    responses = ["Hi there!", "Hey! How can I help you today?", "Greetings!"]
    byes = ["bye", "goodbye", "see you later"]
    user_input = input("You: ").lower()    
    if user_input in greetings:
        bot_response = random.choice(responses)
        print("Bot:", bot_response)
        chat = int(input("Enter 1 to continue the chat\nEnter 0 to exit\n"))
    elif user_input in byes:
        print("Bot: Bye! I hope you have a good day!")
        chat = 0
    else:
        print("Bot: Sorry, I don't understand")
