import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def detect_speech(path_to_file):
    client = speech.SpeechClient()

    with io.open(path_to_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    # You may or may not specify the exact encoding and freq of the recording!
    config = types.RecognitionConfig(\
        encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=None,
        language_code='en-US',
        speech_contexts=[speech.types.SpeechContext(\
            phrases=['poker', 'play'],
        )])

    response = client.recognize(config, audio)
    return {
        'transcript': response.results[0].alternatives[0].transcript,
        'confidence': response.results[0].alternatives[0].confidence
    }

def detect_speech_uri(uri):
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=uri)

    # You may or may not specify the exact encoding and freq of the recording!
    config = types.RecognitionConfig(\
        encoding=enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=None,
        language_code='en-US',
        speech_contexts=[speech.types.SpeechContext(\
            phrases=['poker', 'play'],
        )])

    response = client.recognize(config, audio)
    return {
        'transcript': response.results[0].alternatives[0].transcript,
        'confidence': response.results[0].alternatives[0].confidence
    }

def main():
    print(detect_speech_uri('gs://poker-bot-src-bucket/audio/Play.wav'))

if __name__ == '__main__':
    main()
