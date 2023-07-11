import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from keyboards.main_reply_keyboard import create_reply_keyboard
from keyboards.order_inline_keyboards import select_order_category, select_order_type, select_order_deadline



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

@bot.message_handler(func=lambda message: message.text == "🛠 Создать заказ")
def handle_create_order(message):
    select_order_category(message, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['diplom', 'kursovaya', 'practika', 'laborator', 'another'])
def handle_select_type(call):
    select_order_type(call.message, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['desktop', 'site', 'tgbot', 'console'])
def handle_select_deadline(call):
    select_order_deadline(call.message, bot)


bot.polling()
