message=input("enter your message")
import pyttsx3
engine=pyttsx3.init()
engine.say(message)
engine.runAndWait()