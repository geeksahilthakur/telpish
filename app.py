from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6752205626:AAFmvEgnj6j_jl1WmqSowQeSAQqYW_yo4hQ'
TELEGRAM_CHAT_ID = '5043961881'  # Replace with your actual Telegram chat ID

# Define the form template
form_template = """

<!DOCTYPE html>
<html>
<head>
    <title>Telegram Form</title>
</head>
<body>
    <form id="telegramForm" action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

# Route for displaying the form
@app.route('/')
def show_form():
    return form_template

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        name = request.form['name']
        email = request.form['email']

        # Send the form data to the Telegram bot
        message = f"New form submission:\nName: {name}\nEmail: {email}"
        send_message_to_telegram(message)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def send_message_to_telegram(message):
    telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(telegram_api_url, params=params)
    response.raise_for_status()

# Main function
if __name__ == "__main__":
    app.run(port=5000)
