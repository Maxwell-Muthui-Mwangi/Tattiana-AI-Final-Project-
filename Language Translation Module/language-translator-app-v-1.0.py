from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

text = "Hello, how are you?"
target_language = "es"  # Spanish
translated_text = translate_text(text, target_language)
print(f'Translated Text: {translated_text}')




from google.cloud import speech, texttospeech
import io

def transcribe_speech(speech_file):
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript

def synthesize_speech(text, target_language):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=target_language,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

speech_file = "path/to/your/audiofile.wav"
transcribed_text = transcribe_speech(speech_file)
print(f'Transcribed Text: {transcribed_text}')

target_language = "es"
translated_text = translate_text(transcribed_text, target_language)
print(f'Translated Text: {translated_text}')

synthesize_speech(translated_text, target_language)





from google.cloud import translate
import six

def translate_document(document_path, target_language):
    translate_client = translate.Client()

    with open(document_path, 'rb') as document:
        content = document.read()

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    result = translate_client.translate(
        content,
        target_language=target_language,
        format_="text"  # Assuming text documents; for PDFs or other formats, this can be modified
    )
    return result['translatedText']

document_path = "path/to/your/document.txt"
target_language = "es"
translated_document = translate_document(document_path, target_language)
print(f'Translated Document: {translated_document}')
