# built-in
from typing import List
import io

# local
from audio_manager import *

# thrid party lib
import pandas as pd
from google.cloud import speech

def voice_to_speech(data_generator) -> List[str]:
    """Continuously collect data from the audio stream, into the buffer.
       Reference: https://cloud.google.com/speech-to-text/docs/transcribe-streaming-audio#perform_streaming_speech_recognition_on_an_audio_stream
        Args:
            data_generator: yields audio bytestring data (Maximum size is 20KB for each data yield)
        Returns:
            transcribed string data
    """
    client = speech.SpeechClient()
    
    requests = (
        speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in data_generator
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    streaming_config = speech.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(
        config=streaming_config,
        requests=requests,
    )

    retvals = []
    for response in responses:
        # Detects speech in the audio file
        recognition_alternatives = response.results[0].alternatives if len(response.results) == 1 else []
        # recognition_alternatives : [{x.transcript, x.confidence}]
        recognition_alternatives = sorted(recognition_alternatives, key = lambda x : -x.confidence)
        transcript = recognition_alternatives[0].transcript
        retvals.append(transcript)

    return retvals
