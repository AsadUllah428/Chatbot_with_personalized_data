from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Test Data
def get_bot_response(user_message):
    if "Cloths" in user_message.lower():
        return "We have a wide variety of Cloths, what type do you want ?."
    elif "best seller" in user_message.lower():
        return "Our best-sellers include 'Pants and western shorts'."
    else:
        return "I'm happy to help with your inquiries! What else would you like to know?"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)

