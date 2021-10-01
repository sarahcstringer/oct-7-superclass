import os
import uuid

import twilio.jwt.access_token
import twilio.jwt.access_token.grants
import twilio.rest
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Load environment variables from a `.env` file
load_dotenv()

# Twilio client initialization
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY"]
api_secret = os.environ["TWILIO_API_SECRET"]

# Room settings
ROOM_NAME = "Superclass!"
MAX_PARTICIPANTS = 6

twilio_client = twilio.rest.Client(api_key, api_secret, account_sid)


@app.route("/")
def serve():
    """Render the homepage."""
    return render_template("index.html")


# Start the server when we run this file
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
