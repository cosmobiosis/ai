import pyaudio
import sounddevice
import wave
import numpy as np
import uuid
from typing import Type

# class Talker:
#     def __init__(self, name):
#         self.id = str(uuid.uuid4())
#         self.name = name
    
#     def id(self):
#         return self.id
        
# class Session:
#     def __init__(self):
#         self.id = str(uuid.uuid4())
#         self.dialogues = []
    
#     def push_dialogue(talker: Type[Talker]):
#         pass 

# class Dialogue:
#     def __init__(self):
#         self.talker_id = None
#         self.id = str(uuid.uuid4())

class AudioBuffer:
    def __init__(self, rate, frames):
        self.rate = rate
        self.data = np.frombuffer(b''.join(frames), dtype=np.int16)

class AudioManager:
    def __init__(self):
        self.sessions = {} # session id -> session
        self.FORMAT = pyaudio.paInt16  # Sample format (e.g., 16-bit integer samples)
        self.CHANNEL = 1  # Mono
        self.RATE = 44100
        self.CHUNK_SIZE = 1024
        self.pyaudio = pyaudio.PyAudio()

    def record(self, record_duration_seconds):
        # last_active_ts = time.time()
        stream = self.pyaudio.open(
            format=self.FORMAT,
            channels=self.CHANNEL,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK_SIZE
        )

        frames = []
        # Record audio from the microphone for the specified duration
        for _ in range(0, int(self.RATE / self.CHUNK_SIZE * record_duration_seconds)):
            data = stream.read(self.CHUNK_SIZE)
            frames.append(data)
        stream.stop_stream()
        stream.close()

        return AudioBuffer(self.RATE, frames)

    def play(self, bytes_stream):
        sounddevice.play(bytes_stream, self.RATE)
        sounddevice.wait()

# Initialize PyAudio

if __name__ == "__main__":
    streamReader = AudioManager()
    streamReader.record(3)