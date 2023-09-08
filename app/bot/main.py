# from ..model.init import NeiroDialogBot
import os
import sys
import telebot
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from model.init import NeiroDialogBot

# import ..model.init


bot = telebot.TeleBot('6030990890:AAHNRzVM296wejBzb_tSddYS6C0isT6tPlg')
neiroDialog = NeiroDialogBot('tinkoff-ai/ruDialoGPT-medium')

@bot.message_handler(commands=['start'])   
def main(message):
    neiroDialog.restartBot()
    bot.send_message(message.chat.id, 'Привет, я бот, можешь писать мне что угодно!')

@bot.message_handler()
def info(message):
    bot.send_message(message.chat.id, f'{neiroDialog.replyToTheMessage(message.text)}')


    
    

bot.polling(none_stop=True)