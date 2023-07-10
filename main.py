import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from keyboards.reply import creat_reply_keybourd

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler(message, bot)
    creat_reply_keybourd(message, bot)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_handler(message, bot)

bot.polling()
