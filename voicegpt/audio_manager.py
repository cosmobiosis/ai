import pyaudio
import sounddevice
import wave
import numpy as np
import uuid
from typing import Type

import math

class AudioBuffer:
    def __init__(self, rate, frames):
        self.rate = rate
        self.data = np.frombuffer(b''.join(frames), dtype=np.int16)

class MicrophoneStream:
    def __init__(self):
        self.sessions = {} # session id -> session
        self.FORMAT = pyaudio.paInt16  # Sample format (e.g., 16-bit integer samples)
        self.CHANNEL = 1  # Mono
        self.RATE = 44100
        self.CHUNK_SIZE = 1024
        self.pyaudio = pyaudio.PyAudio()

    def record(self, record_duration_seconds, seconds_per_buffer):
        """Generator that records data for x seconds
            Returns:
                yielded AudioBuffer
        """
        # last_active_ts = time.time()
        stream = self.pyaudio.open(
            format=self.FORMAT,
            channels=self.CHANNEL,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK_SIZE
        )

        if seconds_per_buffer is None:
            seconds_per_buffer = record_duration_seconds

        num_buffer = int(math.ceil(record_duration_seconds / seconds_per_buffer))
        # Record audio from the microphone for the specified duration
        for i in range(0, num_buffer):
            frames = []
            for _ in range(0, int(self.RATE / self.CHUNK_SIZE * seconds_per_buffer)):
                data = stream.read(self.CHUNK_SIZE)
                frames.append(data)
            yield AudioBuffer(self.RATE, frames)
        
        stream.stop_stream()
        stream.close()

    def play(self, bytes_stream):
        sounddevice.play(bytes_stream, self.RATE)
        sounddevice.wait()

# Initialize PyAudio

if __name__ == "__main__":
    streamReader = MicrophoneStream()
    streamReader.record(3)