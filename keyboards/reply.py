from telebot import types
def creat_reply_keybourd(message):
    # Создание reply-клавиатуры
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    buttons = ['Button 1', 'Button 2', 'Button 3', 'Button 4']
    # Добавление кнопок на клавиатуру
    keyboard.add(*buttons)