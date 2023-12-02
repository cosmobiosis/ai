# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
caller_phone_number = os.environ['TWILIO_DEV_CALLER_PHONE_NUMBER']
callee_phone_number = os.environ['TWILIO_DEV_CALLEE_PHONE_NUMBER']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_=callee_phone_number,
                        to=caller_phone_number
                    )
print(call.sid)
