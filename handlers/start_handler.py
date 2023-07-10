import telebot
def start_handler(message, bot):
    user_mention = message.from_user.first_name
    start1 = f"🖐 Привет, *{user_mention}*! "
    start2 = "Я бот студии разработки *«Ctrl C + Ctrl V»*. "
    start3 = "Я помогу тебе в создании заказов на разработку *Desktop приложений*, *сайтов*, *телеграмм ботов* и многого другого."
    start_message = start1 + start2 + start3
    bot.send_message(message.chat.id, start_message, parse_mode="Markdown")
