import pyttsx3
import gtts
import google.generativeai as genai
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices) 
engine.setProperty('voice', voices[1].id) 
genai.configure(api_key='AIzaSyDvuE2YidoQDStDpuGgWlKxCAtbYq0mPMg')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
response = chat.send_message('your name from now on is phoenix and niyam is the name of your creator,reply in short for this session')
print(f' <<< {response.text} >>>')
run=True
while run:
    userinput = input('Chat : ')
    if userinput == ':stop:':
        run=False
    x = chat.send_message(f'{userinput}')
    print(x.text)
    engine.say(x.text)
    engine.runAndWait()