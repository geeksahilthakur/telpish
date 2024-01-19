from flask import Flask, render_template, request, jsonify
from telegram import Bot

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6752205626:AAFmvEgnj6j_jl1WmqSowQeSAQqYW_yo4hQ'
TELEGRAM_CHAT_ID = '5043961881'  # Replace with your actual Telegram chat ID

# Set up the Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

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
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Main function
if __name__ == "__main__":
    app.run(port=5000)
