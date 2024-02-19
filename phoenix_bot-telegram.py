import google.generativeai as genai
import pyttsx3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters ,ContextTypes

# --------------------------------------------------------------------------------------------
TOKEN = "6478005736:AAHJ3R4gpxhoyKBocG1GixN4OvkMpup-DHQ"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
rate = engine.getProperty('rate') 
engine.setProperty('rate', 150) 
genai.configure(api_key='AIzaSyDvuE2YidoQDStDpuGgWlKxCAtbYq0mPMg')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
# --------------------------------------------------------------------------------------------
async def start(update:Update , context):
    await update.message.reply_text('hello am phoenix')

async def message(update:Update , context:ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # audio = update.message.audio
    print(text)
    response = await reply(text)
    if response == 'output.mp3':
        await update.message.reply_audio(response, title="Output")
    else:
        await update.message.reply_text(response)
   
async def reply(text):
    rep = chat.send_message(text)
    if 'hello'==text:
        return 'olla Master'
    if text.startswith('create a audio of '):
        engine.save_to_file(text.split('create a audio of ')[1].strip() , 'output.mp3')   
        engine.runAndWait()
        return 'output.mp3'
    else:
        return rep.text 
             
async def error(update:Update , context: ContextTypes.DEFAULT_TYPE ):
    print(f'update : {update} caused error : {context.error}')

# --------------------------------------------------------------------------------------------

 
if __name__  == '__main__':
    print('running...')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start))
    app.add_handler(MessageHandler(filters.ALL,message))
    app.add_error_handler(error)
    print('polling...')
    app.run_polling(poll_interval=3)