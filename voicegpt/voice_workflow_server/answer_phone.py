from flask import abort, Flask, request
from functools import wraps
from twilio.twiml.voice_response import VoiceResponse
from twilio.request_validator import RequestValidator

app = Flask(__name__)

# def validate_twilio_request(f):
#     """Validates that incoming requests genuinely originated from Twilio"""
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))

#         request_valid = validator.validate(
#             request.url,
#             request.form,
#             request.headers.get('X-TWILIO-SIGNATURE', ''))

#         if request_valid:
#             return f(*args, **kwargs)
#         else:
#             return abort(403)
#     return decorated_function

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("This feature is particularly useful for businesses and developers who need to implement sophisticated voice interaction systems, analyze call data in real-time, or integrate phone calls with advanced digital systems. The ability to process audio streams on the fly opens up numerous possibilities for creating interactive and responsive voice applications.", voice='Polly.Amy')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
