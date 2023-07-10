from telebot import types
def select_order_category(message, bot):

    select_category_keyboard = types.InlineKeyboardMarkup()
    diplom_button = types.InlineKeyboardButton('Дипломная работа', callback_data='diplom')
    kurs_button= types.InlineKeyboardButton('Курсовая работа', callback_data='kursovaya')
    practika_button = types.InlineKeyboardButton('Практика(УП/ПП)', callback_data='practika')
    lab_button = types.InlineKeyboardButton('Лабораторная работа', callback_data='laborator')
    another_button = types.InlineKeyboardButton('Другое', callback_data='another')

    select_category_keyboard.add(diplom_button, kurs_button, practika_button, lab_button, another_button)

    bot.send_message(message.chat.id, 'Выберите категорию работ:', reply_markup=select_category_keyboard)
