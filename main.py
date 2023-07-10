import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from keyboards.reply import create_reply_keyboard
from handlers.create_order import select_order_category
from handlers.create_order import get_selected_category
from handlers.create_order import get_selected_type
from handlers.create_order import get_selected_deadline


load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    main_keyboard = create_reply_keyboard()
    start_handler(message, bot, main_keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['diplom', 'kursovaya', 'practika', 'laborator', 'another'])
def handle_order_category(call):
    get_selected_category(call, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['site', 'consol', 'dekstop', 'telegram_bot', 'another'])
def handle_order_type(call):
    get_selected_type(call, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['<1_week', '1-2_week', '2_week-1_month', '1-2_month', '2_month_and_more'])
def handle_order_deadline(call):
    get_selected_deadline(call, bot)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_handler(message, bot)

@bot.message_handler(func=lambda message: message.text == "🛠 Создать заказ")
def handle_create_order(message):
    select_order_category(message, bot)

bot.polling() #777
