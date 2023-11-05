import pandas as pd
from google.cloud import speech

from marvin_classifier import *
from voice_to_speech import *
from buffer_generator import *
from speech_to_voice import *

from marvin_classifier import *

from audio_manager import *

import scipy.io.wavfile as scipy_wav
import wave
import pyaudio
import sounddevice

from pydub import AudioSegment
from pydub.playback import play
import io

if __name__ == "__main__":
    microphone_stream = MicrophoneStream()
    print("Start Recording...")
    audio_buffer_channel = microphone_stream.record(record_duration_seconds=10, seconds_per_buffer=1)
    raw_bytes_channel = AudioBufferMiddleware().convert_audio_buffer(audio_buffer_channel)
    transcribed_text_channel = voice_to_speech(raw_bytes_channel)

    prompt = ""
    for transcribed_text in transcribed_text_channel:
        print("transcribed (streaming): ", transcribed_text)
        if transcribed_text != "":
            prompt = transcribed_text
    
    print("transcribed (final prompt): ", prompt)
    robot_resp = get_customer_intent_hardcoded_response(prompt=prompt)
    response = speech_to_voice(input_string=robot_resp)
    synthesized_voice = AudioSegment.from_file(io.BytesIO(response), format="mp3")
    play(synthesized_voice)