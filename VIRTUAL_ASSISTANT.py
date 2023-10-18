import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia as wp
import pyjokes
from datetime import datetime
import sys


listener= sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    with sr.Microphone() as source:
        print("Waiting for your message...")
        try:
            audio = listener.listen(source, timeout=5)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said: {}".format(command))
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Google Speech Recognition could not recognize your audio")
            talk("Google Speech Recognition could not recognize your audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
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
      info=wp.summary(person,2)
      print(info)
      talk(info)
   elif 'are you single' in command:
      talk('no i am in relationship with wifi')
   elif 'joke' in command:
      jokes=pyjokes.get_joke()
      print(jokes)
      talk(jokes)
   elif 'rest'in command:
      talk("off to work,rest time")
      sys.exit()
      
talk("hai iam alexa how can i help you")
while True:
   alexa()
