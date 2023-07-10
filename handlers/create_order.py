from telebot import types
product = {}
def select_order_category(message, bot):

    select_category_keyboard = types.InlineKeyboardMarkup()
    categories = {
        'Дипломная работа': 'diplom',
        'Курсовая работа': 'kursovaya',
        'Практика(УП/ПП)': 'practika',
        'Лабораторная работа': 'laborator',
        'Другое': 'another'
    }
    for category, callback_data in categories.items():
        button = types.InlineKeyboardButton(category, callback_data=callback_data)
        select_category_keyboard.add(button)

    bot.send_message(message.chat.id, 'Выберите категорию работы:', reply_markup=select_category_keyboard)



def get_selected_category(call, bot):
    global product
    message = call.message
    product['category'] = call.data
    select_order_type(message, bot)

def select_order_type(message, bot):

    select_type_keyboard = types.InlineKeyboardMarkup()
    product_types = {
        'Сайт': 'site',
        'Консольное приложение': 'consol',
        'Dekstop-приложение': 'dekstop',
        'Telegram-бот': 'telegram_bot',
        'Другое': 'another'
    }
    for product_type, callback_data in  product_types.items():
        button = types.InlineKeyboardButton(product_type, callback_data=callback_data)
        select_type_keyboard.add(button)

    bot.send_message(message.chat.id, 'Выберите тип работы:', reply_markup=select_type_keyboard)


def get_selected_type(call, bot):
    global product
    message = call.message
    product['type'] = call.data
    select_order_deadline(message, bot)

def select_order_deadline(message, bot):

    select_deadline_keyboard = types.InlineKeyboardMarkup()
    deadlines = {
        '<1 недели': '<1_week',
        '1-2 недели': '1-2_week',
        '2 недели - 1 месяц': '2_week-1_month',
        '1-2 месяца': '1-2_month',
        '2 месяца и более': '2_month_and_more'
    }
    for deadline, callback_data in deadlines.items():
        button = types.InlineKeyboardButton(deadline, callback_data=callback_data)
        select_deadline_keyboard.add(button)
    bot.send_message(message.chat.id, 'Выберите конечный срок:', reply_markup=select_deadline_keyboard)


def get_selected_deadline(call, bot):
    global product
    message = call.message
    product['deadline'] = call.data
    total_cost()
    select_order_deadline(message, bot)
def total_cost():
    global product
    cost = 1
    if product['category'] == 'Дипломная работа':
        if product['type'] == 'Сайт':
            cost = 15000
        if product['type'] == 'Dekstop-приложение':
            cost = 10000
        if product['type'] == 'Консольное приложение':
            cost = 8000
        if product['type'] == 'Telegram-бот':
            cost = 8000

    if product['category'] == 'Курсовая работа':
        if product['type'] == 'Сайт':
            cost = 4000
        if product['type'] == 'Dekstop-приложение':
            cost = 5000
        if product['type'] == 'Консольное приложение':
            cost = 3000
        if product['type'] == 'Telegram-бот':
            cost = 3000
    if product['category'] == 'Практика(УП/ПП)':
        if product['type'] == 'Сайт':
            cost = 3000
        if product['type'] == 'Dekstop-приложение':
            cost = 3500
        if product['type'] == 'Консольное приложение':
            cost = 3000
        if product['type'] == 'Telegram-бот':
            cost = 2500
    if product['category'] == 'Лабораторная работа':
        if product['type'] == 'Сайт':
            cost = 500
        if product['type'] == 'Dekstop-приложение':
            cost = 500
        if product['type'] == 'Консольное приложение':
            cost = 500
        if product['type'] == 'Telegram-бот':
            cost = 500
    if  product['deadline'] == '<1_week' or ( product['deadline'] == '1-2_week' and product['category'] == 'Дипломная работа'):
        cost *= 2
    elif  product['deadline'] == '2_week-1_month':
        cost *= 0.7
    return cost
def select_order_deadline(message, bot):
    select_total_keyboard = types.InlineKeyboardMarkup()
    chern_button = types.InlineKeyboardButton('<1 недели', callback_data='<1_week')
    go_button = types.InlineKeyboardButton('1-2 недели', callback_data='1-2_week')
    select_total_keyboard.add(chern_button, go_button)
    text = f'Вид работы: {product["category"]}\nТип работы: {product["type"]}\nКонечный срок: {product["deadline"]}\nСтоимость: {total_cost()} рублей'


    bot.send_message(message.chat.id, text, reply_markup=select_total_keyboard)

'''
Хендлеры
@bot.callback_query_handler(func=lambda call: call.data in ['diplom', 'kursovaya', 'practika', 'laborator', 'another'])
@bot.callback_query_handler(func=lambda call: call.data in ['site', 'consol', 'dekstop', 'telegram_bot', 'another'])
@bot.callback_query_handler(func=lambda call: call.data in ['<1_week', '1-2_week', '2_week-1_month', '1-2_month', '2_month_and_more'])
'''