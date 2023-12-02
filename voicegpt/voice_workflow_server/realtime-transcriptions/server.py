import base64
import json
import threading

from flask import Flask, render_template
from flask_sockets import Sockets

#from google.cloud.speech import RecognitionConfig, StreamingRecognitionConfig

from SpeechClientBridge import SpeechClientBridge

from twilio.twiml.voice_response import VoiceResponse, Connect

from twilio.request_validator import RequestValidator

HTTP_SERVER_PORT = 5002

# config = RecognitionConfig(
#     encoding=RecognitionConfig.AudioEncoding.MULAW,
#     sample_rate_hertz=8000,
#     language_code="en-US",
# )
# streaming_config = StreamingRecognitionConfig(config=config, interim_results=True)

app = Flask(__name__)
sockets = Sockets(app)

@app.route("/stream", methods=["POST"])
def return_stream():
    print("POST STREAM TwiML 103")
    response = VoiceResponse()
    connect = Connect()
    connect.stream(url='wss://3911-2601-8c-487e-b430-7506-72d5-9601-5495.ngrok-free.app/audiostream')
    response.append(connect)
    return response

    # return render_template("streams.xml")

    # resp = VoiceResponse()

    # # Read a message aloud to the caller
    # resp.say("This feature is particularly useful for businesses and developers who need to implement sophisticated voice interaction systems, analyze call data in real-time, or integrate phone calls with advanced digital systems. The ability to process audio streams on the fly opens up numerous possibilities for creating interactive and responsive voice applications.", voice='Polly.Amy')

    # return str(resp)

def on_transcription_response(response):
    return
    # if not response.results:
    #     return

    # result = response.results[0]
    # if not result.alternatives:
    #     return

    # transcription = result.alternatives[0].transcript
    # print("Transcription: " + transcription)


@sockets.route("/audiostream")
def transcript(ws):
    print("WS connection opened")
    bridge = SpeechClientBridge(streaming_config, on_transcription_response)
    t = threading.Thread(target=bridge.start)
    t.start()

    while not ws.closed:
        message = ws.receive()
        if message is None:
            bridge.add_request(None)
            break

        data = json.loads(message)
        if data["event"] in ("connected", "start"):
            print(f"Media WS: Received event '{data['event']}': {message}")
            continue
        if data["event"] == "media":
            media = data["media"]
            chunk = base64.b64decode(media["payload"])
            bridge.add_request(chunk)
        if data["event"] == "stop":
            print(f"Media WS: Received event 'stop': {message}")
            print("Stopping...")
            break

    t.join()
    bridge.terminate()
    print("WS connection closed")

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(
        ("", HTTP_SERVER_PORT), app, handler_class=WebSocketHandler
    )
    print("Server listening on: http://localhost:" + str(HTTP_SERVER_PORT))
    server.serve_forever()
