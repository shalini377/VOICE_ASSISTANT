import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia as wp
import pyjokes
from datetime import datetime


listener= sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
      try:
        with sr.Microphone() as source:
          print("waiting for your message...")
          voice =listener.listen(source)
          command =listener.recognize_google(voice)
          command=command.lower()
          if 'alexa' in command:
             print(command)
             command=command.replace('alexa','')
      except:
         print("sorry couldn't get you, Try again....")
      return command


def alexa():
   command=take_command()
   print(command)
   if 'play' in command:
      song=command.replace('play','')
      talk('playing'+song)
      pywhatkit.playonyt(song)
   elif 'time' in command:
      time=datetime.now().strftime('%I:%M %p')
      print(time)
      talk('current time is' +time)
   elif 'date' in command:
      day =datetime.now().strftime('%B %d,%Y')
      print(day)
      talk("today's date is"+ day)
   elif 'who is' in command:
      person=command.replace('who is','')
      info=wp.summary(person,3)
      print(info)
      talk(info)
   elif 'are you single' in command:
      talk('no I am in relationship with wifi')
   elif 'joke' in command:
      jokes=pyjokes.get_joke()
      print(jokes)
      talk(jokes)
   elif 'rest' in command:
      talk("off to work rest time")
      
talk("hello iam alexa how can i help you")
while True:
   alexa()
