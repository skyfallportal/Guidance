import random

# Define the chatbot class
class Chatbot:
    # Define the constructor to initialize the chatbot's name
    def __init__(self, name):
        self.name = name
    
    # Define the function to respond to user input
    def respond(self, message):
        # Convert the user input to lowercase
        message = message.lower()
        
        # Define a list of responses to greetings
        greetings = ['hello!', 'hi there!', 'hey!', 'greetings!']
        
        # Define a list of responses to questions
        questions = ['I am not sure, can you provide more information?', 'I am sorry, I do not have that information.', 
                     'I am afraid I cannot help you with that.', 'I think that is beyond my capabilities.']
        
        # Define a list of responses to goodbye
        goodbyes = ['Goodbye!', 'See you soon!', 'Take care!', 'Bye!']
        
        # Check if the user input contains a greeting keyword
        if any(word in message for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(greetings)
        
        # Check if the user input contains a question keyword
        if any(word in message for word in ['what', 'where', 'when', 'why', 'how']):
            return random.choice(questions)
        
        # Check if the user input contains a goodbye keyword
        if any(word in message for word in ['goodbye', 'bye', 'see you', 'take care']):
            return random.choice(goodbyes)
        
        # If no keyword is found, respond with a generic message
        return "I'm sorry, I did not understand your request."

# Create an instance of the chatbot
chatbot = Chatbot('Customer Service Bot')

# Define a loop to simulate a conversation with the user
while True:
    # Get the user input
    message = input(chatbot.name + ': ')
    
    # Exit the loop if the user says goodbye
    if any(word in message.lower() for word in ['goodbye', 'bye', 'see you', 'take care']):
        print(chatbot.respond(message))
        break
    
    # Get the chatbot's response
    response = chatbot.respond(message)
    
    # Print the chatbot's response
    print(chatbot.name + ': ' + response)
