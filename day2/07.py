import cowsay
message=input("enter your message")
cowsay.meow(message)
import pyttsx3
engine=pyttsx3.init()
engine.say(message)
engine.runAndWait()