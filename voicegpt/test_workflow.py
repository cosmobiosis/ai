import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

import flytekit.extras.sklearn
from flytekit import task, workflow
from google.cloud import speech

from marvin_classifier import *
from voice_to_speech import *
from speech_to_voice import *

@workflow
def test_workflow():
    transcript = voice_to_speech(gcs_uri="gs://wsu78_test_bucket/speech/a0.wav")
    robot_resp = get_response_text(prompt=transcript)
    speech_to_voice(input_string=robot_resp)

if __name__ == "__main__":
    test_workflow()