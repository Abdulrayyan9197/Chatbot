import nltk
import re

# Define response rules
responses = {
    "greeting": ["Hi! How can I help you today?", "Hello! Need any assistance?"],
    "store_hours": ["Our store is open from 9 AM to 9 PM, Monday to Saturday."],
    "return_policy": ["You can return products within 30 days of purchase with a receipt."],
    "order_status": ["To check your order status, please log in to your account."],
    "product_availability": ["Please specify the product name to check availability."],
    "contact_info": ["You can reach us at support@example.com or call 123-456-7890."],
    "default": ["I'm sorry, I didn't understand that. Could you rephrase?"]
}

# Define keywords for each intent
keywords = {
    "greeting": ["hi", "hello", "hey"],
    "store_hours": ["open", "working hours", "time", "when"],
    "return_policy": ["return", "refund", "exchange"],
    "order_status": ["order", "track", "status"],
    "product_availability": ["available", "in stock", "have"],
    "contact_info": ["contact", "email", "phone", "number"]
}

def preprocess(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r"[^\w\s]", "", user_input)  # Remove punctuation
    return user_input

def get_response(user_input):
    user_input = preprocess(user_input)
    for intent, keys in keywords.items():
        for word in keys:
            if word in user_input:
                return responses[intent][0]
    return responses["default"][0]

# Main loop
print("Customer Service Bot: Hello! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Customer Service Bot: Goodbye! Have a nice day.")
        break
    response = get_response(user_input)
    print("Customer Service Bot:", response)
