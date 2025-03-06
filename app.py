# import openai
# from flask import Flask, render_template, request, jsonify

# # Set up OpenAI API key
# openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

# # Create Flask app
# app = Flask(__name__)

# # Store conversation history to maintain context
# conversation_history = []

# # Define function to interact with OpenAI API
# def get_bot_response(user_message):
#     # Add user's message to conversation history
#     conversation_history.append({'role': 'user', 'content': user_message})

#     # Call the OpenAI API with conversation history
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # You can use gpt-3.5-turbo or another available model
#         messages=conversation_history,
#         max_tokens=150
#     )

#     # Get bot's response and update conversation history
#     bot_message = response['choices'][0]['message']['content']
#     conversation_history.append({'role': 'assistant', 'content': bot_message})

#     return bot_message

# # Home route to display the chat interface
# @app.route('/')
# def index():
#     return render_template('index.html')

# # API route for handling chat requests
# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.form['message']
#     bot_response = get_bot_response(user_message)
#     return jsonify({'response': bot_response})

# if __name__ == "__main__":
#     app.run(debug=True)






from flask import Flask, render_template, request, jsonify

# Create Flask app
app = Flask(__name__)

# Mock function to simulate bot's response
def get_bot_response(user_message):
    if "Cloths" in user_message.lower():
        return "We have a wide variety of Cloths, what type do you want ?."
    elif "best seller" in user_message.lower():
        return "Our best-sellers include 'Pants and western shorts'."
    else:
        return "I'm happy to help with your inquiries! What else would you like to know?"

# Route to display the chat interface
@app.route('/')
def index():
    return render_template('index.html')

# API route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)

