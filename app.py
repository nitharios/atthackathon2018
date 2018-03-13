# NOTE: this example requires PyAudio because it uses the Microphone class
from voices import VOICES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Imports the Google Cloud client library
from os import system
from google.cloud import translate

import speech_recognition as sr
import pyttsx3

def run():
  # Instantiates a client
  translate_client = translate.Client()

  try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    transcription = set_up_mic()
    # The text to translate
    print(transcription)

    if transcription[0:7] == "YouTube":
      driver = webdriver.Chrome("/Users/nniosco/chromedriver")
      search = transcription[8:]
      search.replace(" ", "+")
      driver.get("https://www.youtube.com/results?search_query=" + search)
      driver.implicitly_wait(4) 
    #  element = driver.find_element_by_xpath("//div[@class='yt-thumb video-thumb yt-uix-mouseover-img-wrap']")
      element = driver.find_element_by_class_name('ytd-video-renderer')
      element.click()
      #$('[class="yt-thumb video-thumb yt-uix-mouseover-img-wrap"]').click()
      while 1==1:
        pass
    
    if transcription[0:6] == "Google": 
      driver = webdriver.Chrome("/Users/nniosco/chromedriver")
      search = transcription[7:]
      #for Google we want to translate our results
      # The target language
      lang = detect_language(search)
      print(lang)
      target = 'en'
      # Translates text
      translation = translate_client.translate(
        search,
        target_language=target)
      translatedString = str(format(translation['translatedText'])).replace(" ", "+")
      driver.get("https://www.google.com/search?q=" + translatedString)
      driver.implicitly_wait(4)
      while 1==1:
        pass

    if transcription[0:6] == "Reddit": 
      driver = webdriver.Chrome("/Users/nniosco/chromedriver")
      search = transcription[7:]
      search.replace(" ", "+")
      driver.get("https://www.reddit.com/search?q=" + search + "&sort=relevance&t=all")
      driver.implicitly_wait(4) 
      while 1==1:
        pass
    
    # The target language
    lang = detect_language(transcription)
    print(lang)
    target = 'es'

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
    #print(u'Translation: {}'.format(translation['translatedText']))

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

# obtain audio from the microphone
def set_up_mic():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

  # recognize speech using Google Speech Recognition
  return r.recognize_google(audio)

run()
