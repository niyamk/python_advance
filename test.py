import pyttsx3
import os
engine = pyttsx3.init()
rate = engine.getProperty('rate') 
voices = engine.getProperty('voices') 
engine.setProperty('rate', 150) 
engine.setProperty('voice', voices[1].id) 
# engine.say('himanshu ahhh ahhhhh ahhhhhhhh')
engine.save_to_file('hello my friend','himanshu.mp3')
engine.runAndWait()