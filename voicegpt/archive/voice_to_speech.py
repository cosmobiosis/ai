import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

# import flytekit.extras.sklearn
# from flytekit import task, workflow
from google.cloud import speech

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

from google.cloud import speech

from audio_manager import *
import scipy.io.wavfile as scipy_wav
import io

def voice_to_speech(binary_buffer) -> str:
    # param: 
    # binary_buffer: bytes array MAXIMUM SIZE: 25KB
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    audio = speech.RecognitionAudio(content=binary_buffer)
    # audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    recognition_alternatives = response.results[0].alternatives if len(response.results) == 1 else []
     # recognition_alternatives : [{x.transcript, x.confidence}]
    recognition_alternatives = sorted(recognition_alternatives, key = lambda x : -x.confidence)
    transcript = recognition_alternatives[0].transcript
    return transcript

# @task
# def voice_to_speech_by_url(gcs_uri) -> str:
#     # Instantiates a client
#     client = speech.SpeechClient()

#     # The name of the audio file to transcribe
#     audio = speech.RecognitionAudio(uri=gcs_uri)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         language_code="en-US",
#         max_alternatives=5
#     )

#     # Detects speech in the audio file
#     response = client.recognize(config=config, audio=audio)
#     recognition_alternatives = response.results[0].alternatives if len(response.results) == 1 else []
#      # recognition_alternatives : [{x.transcript, x.confidence}]
#     recognition_alternatives = sorted(recognition_alternatives, key = lambda x : -x.confidence)
#     transcript = recognition_alternatives[0].transcript
#     return transcript

# if __name__ == "__main__":
#     print(voice_to_speech("gs://wsu78_test_bucket/speech/a0.wav"))