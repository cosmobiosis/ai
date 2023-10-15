import pyaudio

class AudioStreamReader:
    def __init__(self):
        self.format = pyaudio.paInt16  # Sample format (e.g., 16-bit integer samples)
        self.channel = 2  # Mono
        self.rate = 44100
        self.chunk_size = 1024

    def record(self):
        pa = pyaudio.PyAudio()
        stream = pa.open(
            format=self.format, 
            channels=self.channel, 
            rate=self.rate, 
            input=True, 
            frames_per_buffer=self.chunk_size
        )
        # stream.start_stream()
        # while stream.is_active():
        #     pass
        # stream.stop_stream()
        # stream.close()
        # self.audio.terminate()


# Initialize PyAudio

if __name__ == "__main__":
    streamReader = AudioStreamReader()
    streamReader.record()