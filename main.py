import telebot

from config import load_config

config = load_config()
bot = telebot.TeleBot(token = config.tg_bot.token, parse_mode = "HTML")
def main():
    bot.polling(none_stop = True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")