# Twilio Video Demo

This is the code written during the live Twilio Video
demo during Twilio's October 7 Superclass.

It creates a simple Video application that creates a virtual
knitting circle and populates each yarn ball with an HTML
video element when a participant enters the Room.

The main branch contains the base code where we began our live demo.
Check out the `superclass-demo` branch to see the completed code that we wrote during the session.

## Running the application

You'll need Python3 to get this running. To install the required
dependencies:

```
python3 -m venv venv  # create a virtual environment
source venv/bin/activate
pip install -r requirements.txt
```

Next, create a `.env` file. You'll put your account
credentials in that file, so that the Flask server can
connect to Twilio.

```
touch .env
```

In the .env file, you'll want these credentials:

```
TWILIO_ACCOUNT_SID=<your account SID>
TWILIO_API_KEY=<your api key>
TWILIO_API_SECRET=<your api key secret>
```

You can find your account SID in the Twilio Console Dashboard: https://www.twilio.com/console

You can create a new API key and get the secret through the
Twilio console: https://www.twilio.com/console/project/api-keys

To run the Flask server:

```
source venv/bin/activate
python server.py
```

This will start a server that you can access on your
local machine at port 5000 (`localhost:5000`).

Can't wait to see what you build with Twilio Video!

## Other Resources

### Troubleshooting

Preflight check API
[Video Diagnostics App](https://www.twilio.com/blog/video-diagnostics-app-reactjs-preflight-api)
[Video Monitor](https://www.npmjs.com/package/@twilio/video-room-monitor)
Network Quality API

### Virtual Backgrounds and Custom Video Filters

General info: https://www.twilio.com/blog/introducing-virtual-backgrounds-browser-based-video-applications
Custom filters: https://www.twilio.com/blog/custom-effect-filters-twilio-programmable-video
Virtual background: https://www.twilio.com/blog/change-background-video-calls-twilio-video-processors-library

### Other Interesting Features

Dominant Speaker Detection
Track Subscription API?
Recordings and compositions?
