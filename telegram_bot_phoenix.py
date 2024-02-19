import pyttsx3
from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai 
# ----------------------------------------------------------------------------------
engine = pyttsx3.init()
genai.configure(api_key='AIzaSyDvuE2YidoQDStDpuGgWlKxCAtbYq0mPMg')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
TOKEN: Final = '6478005736:AAHJ3R4gpxhoyKBocG1GixN4OvkMpup-DHQ'
BOT_USERNAME: Final = '@PhoenixNkBot'
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
async def start_command( update : Update,context : ContextTypes.DEFAULT_TYPE ) : 
    await update.message.reply_text('hello user , am Phoenix!')
    
async def help_command( update: Update , context : ContextTypes.DEFAULT_TYPE ) :
    await update.message.reply_text("How may I help you?")

async def custom_command( update : Update,context : ContextTypes.DEFAULT_TYPE ) : 
    await update.message.reply_text('this is a custom command')
 # ----------------------------------------------------------------------------------
 # ----------------------------------------------------------------------------------
def handle_response(text:str) -> str:
    proccesed:str = text.lower()
    reply = chat.send_message(text)
    
    # default reply
    if 'create a audio file of' in proccesed:
        engine.save_to_file(proccesed.split('create a audio file of')[1])
        engine.runAndWait()
        
    
    # Gemini AI    
    print('----------------- gemini called -----------------')
    return reply.text
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------  
async def handle_message( update:Update , context: ContextTypes.DEFAULT_TYPE ) -> str:
    message_type = update.message.chat.type
    text = update.message.text
    print(f'user ( {update.message.chat.id} in {message_type} : {text} )')
    
    if message_type=='group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME,'').strip()
            response:str = handle_response(new_text)
        else:
            return 
    else:
        response:str = handle_response(text)
    print('bot : ',response)
    await update.message.reply_text(response)   
# ----------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------- 
async def error(update:Update , context: ContextTypes.DEFAULT_TYPE ):
    print(f'update : {update} caused error : {context.error}')
    
if __name__  == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    
    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT , handle_message))
    
    #errors
    app.add_error_handler(error)
    
    print('polling...   ')
    app.run_polling(poll_interval=3)
    
#start - Starts the bot 
#help - Provides help
#custom - This is a Custom Command
