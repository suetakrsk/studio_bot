from telebot import types

def select_order_category(message, bot):

    select_category_keyboard = types.InlineKeyboardMarkup()
    diplom_button = types.InlineKeyboardButton('Дипломная работа', callback_data='diplom')
    kurs_button= types.InlineKeyboardButton('Курсовая работа', callback_data='kursovaya')
    practika_button = types.InlineKeyboardButton('Практика(УП/ПП)', callback_data='practika')
    lab_button = types.InlineKeyboardButton('Лабораторная работа', callback_data='laborator')
    another_button = types.InlineKeyboardButton('Другое', callback_data='another')

    select_category_keyboard.add(diplom_button)
    select_category_keyboard.add(kurs_button)
    select_category_keyboard.add(practika_button)
    select_category_keyboard.add(lab_button)
    select_category_keyboard.add(another_button)

    bot.send_message(message.chat.id, 'Выберите категорию работы:', reply_markup=select_category_keyboard)


product_category = None
def get_select_diplom(call, bot):
    global product_category
    product_category = 'Дипломная работа'
def get_select_kursovaya(call, bot):
    global product_category
    product_category = 'Курсовая работа'
def get_select_practika(call, bot):
    global product_category
    product_category = 'Практика(УП/ПП)'
def get_select_laborator(call, bot):
    global product_category
    product_category = 'Лабораторная работа'
def get_select_another(call, bot):
    global product_category
    product_category = 'Другое'


def select_order_type(message, bot):

    select_type_keyboard = types.InlineKeyboardMarkup()
    site_button = types.InlineKeyboardButton('Сайт', callback_data='site')
    consol_button = types.InlineKeyboardButton('Консольное приложение', callback_data='consol')
    dekstop_button = types.InlineKeyboardButton('Dekstop-приложение', callback_data='dekstop')
    telegram_bot_button= types.InlineKeyboardButton('Telegram-бот', callback_data='telegram_bot')
    another_button = types.InlineKeyboardButton('Другое', callback_data='another')

    select_type_keyboard.add(site_button)
    select_type_keyboard.add(consol_button)
    select_type_keyboard.add(dekstop_button)
    select_type_keyboard.add(telegram_bot_button)

    bot.send_message(message.chat.id, 'Выберите тип работы:', reply_markup=select_type_keyboard)

product_type = None
def get_select_type_site(call, bot):
    global product_type
    product_type = 'Сайт'

def get_select_type_consol(call, bot):
    global product_type
    product_type = 'Консольное приложение'

def get_select_type_dekstop(call, bot):
    global product_type
    product_type = 'Dekstop-приложение'

def get_select_type_telegram_bot(call, bot):
    global product_type
    product_type = 'Telegram-бот'

def select_order_deadline(message, bot):

    select_deadline_keyboard = types.InlineKeyboardMarkup()
    week_button = types.InlineKeyboardButton('<1 недели', callback_data='<1_week')
    week_week_button = types.InlineKeyboardButton('1-2 недели', callback_data='1-2_week')
    week_month_button = types.InlineKeyboardButton('2 недели - 1 месяц', callback_data='2_week-1_month')
    month_month_button = types.InlineKeyboardButton('1-2 месяца', callback_data='1-2_month')
    month_more_button = types.InlineKeyboardButton('2 месяца и более', callback_data='2_month_and_more')

    select_deadline_keyboard.add(week_button)
    select_deadline_keyboard.add(week_week_button)
    select_deadline_keyboard.add(week_month_button)
    select_deadline_keyboard.add(month_month_button)
    select_deadline_keyboard.add(month_more_button)

    bot.send_message(message.chat.id, 'Выберите конечный срок:', reply_markup=select_deadline_keyboard)

product_deadline = None
def get_select_diplom(call, bot):
    global product_deadline
    product_deadline = '<1 недели'
def get_select_kursovaya(call, bot):
    global product_deadline
    product_deadline = '1-2 недели'
def get_select_practika(call, bot):
    global product_deadline
    product_deadline = '2 недели - 1 месяц'
def get_select_laborator(call, bot):
    global product_deadline
    product_deadline = '1-2 месяца'
def get_select_another(call, bot):
    global product_deadline
    product_deadline = '2 месяца и более'

def total_cost():
    global product_category
    global product_type
    global product_deadline
    global cost

    if product_category == 'Дипломная работа':
        if product_type == 'Сайт':
            cost = 15000
        if product_type == 'Dekstop-приложение':
            cost = 10000
        if product_type == 'Консольное приложение':
            cost = 8000
        if product_type == 'Telegram-бот':
            cost = 8000

    if product_category == 'Курсовая работа':
        if product_type == 'Сайт':
            cost = 4000
        if product_type == 'Dekstop-приложение':
            cost = 5000
        if product_type == 'Консольное приложение':
            cost = 3000
        if product_type == 'Telegram-бот':
            cost = 3000
    if product_category == 'Практика(УП/ПП)':
        if product_type == 'Сайт':
            cost = 3000
        if product_type == 'Dekstop-приложение':
            cost = 3500
        if product_type == 'Консольное приложение':
            cost = 3000
        if product_type == 'Telegram-бот':
            cost = 2500
    if product_category == 'Лабораторная работа':
        if product_type == 'Сайт':
            cost = 500
        if product_type == 'Dekstop-приложение':
            cost = 500
        if product_type == 'Консольное приложение':
            cost = 500
        if product_type == 'Telegram-бот':
            cost = 500
    if product_deadline == '<1_week' or (product_deadline == '1-2_week' and product_category == 'Дипломная работа'):
        cost *= 2
    elif product_deadline == '2_week-1_month':
        cost *= 0.7
    return cost
def select_order_deadline(message, bot):
    global product_deadline
    global product_type
    global product_category
    global cost
    select_total_keyboard = types.InlineKeyboardMarkup()
    chern_button = types.InlineKeyboardButton('<1 недели', callback_data='<1_week')
    go_button = types.InlineKeyboardButton('1-2 недели', callback_data='1-2_week')
    select_total_keyboard.add(chern_button, go_button)
    text = f'Вид работы: {product_category}\nТип работы: {product_type}\nКонечный срок: {product_deadline}\n Стоимость: {total_cost()} рублей'

    bot.send_message(message.chat.id, text, reply_markup=select_total_keyboard)

'''
Хендлеры
@bot.callback_query_handler(func=lambda call: call.data in ['diplom', 'kursovaya', 'practika', 'laborator', 'another'])
@bot.callback_query_handler(func=lambda call: call.data in ['site', 'consol', 'dekstop', 'telegram_bot', 'another'])
@bot.callback_query_handler(func=lambda call: call.data in ['<1_week', '1-2_week', '2_week-1_month', '1-2_month', '2_month_and_more'])
'''