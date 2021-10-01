import os

import twilio.rest
from dotenv import load_dotenv

load_dotenv()

secret = os.environ["TWILIO_API_SECRET"]
key = os.environ["TWILIO_API_KEY"]
sid = os.environ["TWILIO_ACCOUNT_SID"]

client = twilio.rest.Client(key, secret, sid)
