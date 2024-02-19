import speech_recognition as sr
import pyttsx3 
import google.generativeai as genai 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
r = sr.Recognizer()
input_method = input('Enter speech for speech input (default type) : ')

# def record_text():
#     while(1): 
#         try:
#             with sr.Microphone() as source:
#                 r.adjust_for_ambient_noise(source, duration=0.2)
#                 audio = r.listen(source)
#                 MyText = r.recognize_google(audio)
#                 return MyText
#                 # print("Did you say ",MyText)
#                 # SpeakText(MyText)
                
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
            
#         except sr.UnknownValueError as e:
#             print(f"unknown error occurred {e} ")
#     return 

def record_text():
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print('listening...')
                audio = r.listen(source)
                text = r.recognize_google(audio)
                return text
        except sr.UnknownValueError:
            print('speak again!')
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google  {e}")
    

genai.configure(api_key='AIzaSyDvuE2YidoQDStDpuGgWlKxCAtbYq0mPMg')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
res = chat.send_message('i am nirved , your creator and your name is Phoenix and during this session reply shortly')
a = 'running'

if input_method.lower().strip()=='speech':
    while(a=='running'):
        text = record_text()    
        if text == 'terminate':
            a = 'terminate'
        res = chat.send_message(text)
        print('-'*100,'\n',res.text)
        engine.say(res.text)
        engine.runAndWait()
else :
    while a=='running':
        text = input('\nENTER : ',end='\n')
        res = chat.send_message(text)
        print(f'Phoenix : {res.text}')