import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from keyboards.reply import create_reply_keyboard

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    main_keyboard = create_reply_keyboard()
    start_handler(message, bot, main_keyboard)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_handler(message, bot)

bot.polling() #777
