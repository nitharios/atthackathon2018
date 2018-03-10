# NOTE: this example requires PyAudio because it uses the Microphone class

# Imports the Google Cloud client library
from os import system
from google.cloud import translate

import speech_recognition as sr
import pyttsx3

def run():
  # Instantiates a client
  translate_client = translate.Client()

  # obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

  # recognize speech using Google Speech Recognition
  try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    transcription = r.recognize_google(audio)
    # The text to translate
    print(transcription)

    # The target language
    lang = detect_language(transcription)
    print(lang)
    target = 'ja'

    # Translates text
    translation = translate_client.translate(
        transcription,
        target_language=target)

    voiceTranslation = format(translation['translatedText'])
    # voices = engine.getProperty('voices')
    # for voice in voices:
      # print(voice.id)
      # print(voice.languages)
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.kyoko')
    engine.say(voiceTranslation)
    engine.runAndWait()
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))

  except sr.UnknownValueError:
    # print("Google Speech Recognition could not understand audio")
    system('say -v Victoria ' + "Google Speech Recognition could not understand audio")
  except sr.RequestError:
    # print("Could not request results from Google Speech Recognition service; {0}".format(e))
    system('say -v Victoria ' + "Could not request results from Google Speech Recognition service")

def detect_language(text):
  # Detects the text's language.
  translate_client = translate.Client()

  # Text can also be a sequence of strings, in which case this method
  # will return a sequence of results for each text.
  language = translate_client.detect_language(text)
  return language

run()