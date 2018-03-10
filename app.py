# NOTE: this example requires PyAudio because it uses the Microphone class

# Imports the Google Cloud client library
from os import system
import speech_recognition as sr
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
  # for testing purposes, we're just using the default API key
  # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
  # instead of `r.recognize_google(audio)`
  print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
  # The text to translate
  text = r.recognize_google(audio)
  system('say -v Victoria ' + r.recognize_google(audio))

  # The target language
  target = 'ja'

  # Translates some text into Russian
  translation = translate_client.translate(
      text,
      target_language=target)

  print(u'Text: {}'.format(text))
  print(u'Translation: {}'.format(translation['translatedText']))

except sr.UnknownValueError:
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print(
    "Could not request results from Google Speech Recognition service; {0}".format(e))