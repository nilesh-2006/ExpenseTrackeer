import datetime
import time 

name = input("Welcome, Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon", name)
elif 17 <= presentHour <= 20:
    print("Good Evening", name)
else:
    print("Good Night", name)

print("***Welcome to Rule Based Chatbot***")   
print("You can ask me basic questions, Type 'bye' to exit from the bot")

# Chatbot Memory (Dictionary of Responses)
responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine, Thank you!",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep going! Every bug in your project makes you a better developer.",

    # EMOTION RESPONSES
    "happy": "Great! Happiness suits you 😊",
    "sad": "I'm sorry to hear that. Everything will be okay ❤️ Stay strong!",

    "function kya hote hai": "Jakar Chapter 7 padho 😄",

    # NEW QUESTIONS
    "what is python": "Python is a high-level programming language used in AI, ML, data science, and development.",
    "your name": "My name is Rule-Based Chatbot 1.0 🤖",
    "time kya hua": f"Abhi time ho raha hai: {datetime.datetime.now().strftime('%H:%M:%S')}"
}

# Function to get chatbot response
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am sorry, I don't understand your question."

# Take user input
while True:
    userInput = input("Please ask your question: ")

    # 1 second delay before responding
    time.sleep(1)

    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break
