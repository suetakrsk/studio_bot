import telebot
from config import oad_config


config = load_config()
bot = telebot.TeleBot(token=config.tg_bot.token, parse_mode="HTML")

# Добавьте хендлер в бота

bot.set_update_listener(handle_start)

def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")