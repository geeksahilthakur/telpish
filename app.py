from flask import Flask, render_template, request
from telegram import Bot

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6446584536:AAGCLNnVtJ-0yMgQv2xNjL6aYAe1gt234Nw'
TELEGRAM_CHAT_ID = '6446584536'  # Replace with your actual Telegram chat ID

# Set up the Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# HTML form
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Telegram Form</title>
</head>
<body>
    <form action="/submit" method="post">
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
    return html_form

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']

    # Send the form data to the Telegram bot
    message = f"New form submission:\nName: {name}\nEmail: {email}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

    return 'Form submitted successfully!'

# Main function
if __name__ == "__main__":
    app.run(port=5000)
