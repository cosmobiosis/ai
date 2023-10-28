import pandas as pd
from google.cloud import speech

from marvin_classifier import *
from voice_to_speech import *
from buffer_generator import *
# from speech_to_voice import *

from marvin_classifier import *

from audio_manager import *

import scipy.io.wavfile as scipy_wav
import wave
import pyaudio
import sounddevice

if __name__ == "__main__":
    recorder = MicrophoneStream()
    print("Start Recording...")
    audio_buffer_channel = recorder.record(record_duration_seconds=10, seconds_per_buffer=1)
    raw_bytes_channel = AudioBufferMiddleware().convert_audio_buffer(audio_buffer_channel)
    transcribed_text_channel = voice_to_speech(raw_bytes_channel)
    for transcribed_text in transcribed_text_channel:
        print(transcribed_text)
    # robot_resp = get_response_text(prompt=transcript)
    # speech_to_voice(input_string=robot_resp)