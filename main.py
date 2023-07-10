import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from keyboards.reply import create_reply_keyboard
from handlers.create_order import select_order_category

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    main_keyboard = create_reply_keyboard()
    start_handler(message, bot, main_keyboard)


@bot.message_handler(commands=['help'])
def handle_help(message):
    help_handler(message, bot)

@bot.message_handler(func=lambda message: message.text == "🛠 Создать заказ")
def handle_create_order(message):
    select_order_category(message, bot)

bot.polling() #777
