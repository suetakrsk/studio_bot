from telebot import types
from main import bot
import telebot


@telebot.message_handler(commands=['start'])
def handle_start(message):
    response = "Привет! Я телеграмм бот"
    bot.send_message(message.chat.id, response)