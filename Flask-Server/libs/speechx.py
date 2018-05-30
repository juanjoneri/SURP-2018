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
        language_code='en-US')

    response = client.recognize(config, audio)
    print(response.results)

    return

def main():
    for k, v in vars(enums.RecognitionConfig.AudioEncoding).items():
        pass
    detect_speech('../../Speech-Commands/Play.flac')

if __name__ == '__main__':
    main()