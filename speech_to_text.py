import speech_recognition as sr
import pyttsx3 
r = sr.Recognizer() 

def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

def record_text():
    while(1): 
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
                # print("Did you say ",MyText)
                # SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
    return 
def output(text):
    f = open('output.txt','a')
    f.write(text)
    f.write('\n')
    return 

while(1):
    text = record_text()
    output(text)
    print(text)