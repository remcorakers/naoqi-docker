from google.cloud import texttospeech
import os
import io
import playsound

# This file contains an example on how to do Text-to-Speech using the Google Cloud platform.
# A MP3 file is regenerated and saved to output.mp3
# There are two ways to send text to Google:
# Simple text.
# SSML Text.
# With SSML you can customize your text. For example, you can add a delay between words or emphasize certain words.


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "creds.json"
language = 'nl-NL'

client = texttospeech.TextToSpeechClient()
file_path = 'output.mp3'


# [START tts_synthesize_text]
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=0.75)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with io.open(file_path, 'wb+') as out:
        out.write(response.audio_content)
        print('Audio content written to file: ' + str(file_path))
    playsound.playsound(file_path, True)
    os.remove(file_path)


# [START tts_synthesize_ssml]
def synthesize_ssml(ssml):
    """Synthesizes speech from the input string of ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=0.75)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    file_path = 'output2.mp3'
    with io.open(file_path, 'wb+') as out:
        out.write(response.audio_content)
        print('Audio content written to file: ' + str(file_path))
    playsound.playsound(file_path, True)
    os.remove(file_path)

text="Hoi, ik ben Alice"
ssml_text="<speak>Hallo, hoe gaat het met je?<break time='200ms' />" \
          "Met mij gaat het erg goed.</speak>"

synthesize_text(text)

synthesize_ssml(ssml_text)