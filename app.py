# NOTE: this example requires PyAudio because it uses the Microphone class

# Imports the Google Cloud client library
from os import system
from google.cloud import translate

import speech_recognition as sr
import pyttsx3

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
  text = r.recognize_google(audio)
  # The text to translate
  print(text)
  # system('say -v Victoria ' + r.recognize_google(audio))

  # The target language
  target = 'ja'

  # Translates text
  translation = translate_client.translate(
      text,
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
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print(
    "Could not request results from Google Speech Recognition service; {0}".format(e))
