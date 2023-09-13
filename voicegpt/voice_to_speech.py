import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

import flytekit.extras.sklearn
from flytekit import task, workflow
from google.cloud import speech

@task
def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    gcs_uri = "gs://wsu78_test_bucket/speech/a0.wav"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        max_alternatives=5
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    recognition_alternatives = response.results[0].alternatives if len(response.results) == 1 else []
     # recognition_alternatives : [{x.transcript, x.confidence}]
    recognition_alternatives = sorted(recognition_alternatives, key = lambda x : -x.confidence)
    transcript = recognition_alternatives[0].transcript

if __name__ == "__main__":
    run_quickstart()