import numpy as np
import uuid
from typing import Type

import scipy.io.wavfile as scipy_wav
import wave
import pyaudio
import sounddevice
import io

class AudioBufferMiddleware:
    def __init__(self):
        pass

    def convert_audio_buffer(self, channel):
        """Generator that wraps binary buffer in a generator
            Args:
                channel: generator that yields data
            Returns:
                yielded binary_buffer: yielded bytestring
        """
        for audio_buffer in channel:
            result = io.BytesIO()
            scipy_wav.write(result, audio_buffer.rate, audio_buffer.data)
            binary_buffer = result.getvalue()
            yield binary_buffer
