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
    recorder = AudioManager()
    print("Start Recording...")
    audio_buffer = recorder.record(3)
    result = io.BytesIO()
    scipy_wav.write(result, audio_buffer.rate, audio_buffer.data)
    binary_buffer = result.getvalue()

    generator = BufferGenerator().generator_for_one_trunk(binary_buffer)
    print(voice_to_speech(generator))

    # robot_resp = get_response_text(prompt=transcript)
    # speech_to_voice(input_string=robot_resp)