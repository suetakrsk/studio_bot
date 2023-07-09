import telebot
from handlers.start_handler import handle_start

TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)


bot.add_message_handler(handle_start)

bot.polling()