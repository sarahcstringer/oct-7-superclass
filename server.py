import os

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

def find_or_create_room():
    try:
        room = twilio_client.video.rooms(ROOM_NAME).fetch()
    except twilio.base.exceptions.TwilioRestException:
        room = twilio_client.video.rooms.create(
            unique_name=ROOM_NAME,
            type="group",
            max_participants=MAX_PARTICIPANTS
        )
    print(f"{room.unique_name} has {len(room.participants.list())} participants")


@app.route("/")
def serve():
    """Render the homepage."""
    find_or_create_room()
    return render_template("index.html")

@app.route("/token", methods=["POST"])
def generate_access_token():
    identity = request.json.get("identity")
    access_token = twilio.jwt.access_token.AccessToken(
        account_sid, api_key, api_secret, identity=identity
    )
    video_grant = twilio.jwt.access_token.grants.VideoGrant(room=ROOM_NAME)
    access_token.add_grant(video_grant)
    return {"token": access_token.to_jwt()}


# Start the server when we run this file
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
