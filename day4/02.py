message=input("enter your message")
import wikipedia
result=wikipedia.summary(message, sentences=3)
import pyttsx3
engine=pyttsx3.init()
engine.say(result)
engine.runAndWait()
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)      
   #changing index, changes voices. 1 for female 
print(result)