from keyboards.order_inline_keyboards import select_order_type, select_order_deadline

infO_product = {
    'Категория работы': None,
    'Тип работы': None,
    'Сроки': None,
    'Расчетная стоимость': None
}
categoru_texts= {
    'diplom': ['Дипломная работа', 9000],
    'kursovaya': ['Курсовая работа', 4000],
    'practika': ['Практика(УП/ПП)', 2000],
    'laborator': ['Лабораторная работа', 500],
    'another': ['Другое', 3000]
}
type_texts= {
    'site': 'Сайт',
    'desktop': 'Desktop приложение',
    'tgbot': 'Telegram бот',
    'console': 'Консольное приложение',

}
deadline_text = {
    'min1week': ['Меньше 1 недели', 2],
    'odna_dve_week': ['1-2 недели', 1.5],
    'two_week_month': ['2 недели - 1 месяц', 1.2],
    'month': ['1-2 месяца', 1],
    'two-month_more': ['2 месяца и более', 0.9]
}

def choise_order_category(call, bot):
    global infO_product
    global categoru_texts
    category = call.data
    infO_product['Категория работы'] = categoru_texts[category][0]
    infO_product['Расчетная стоимость'] = categoru_texts[category][1]


def choise_order_type(call, bot):
    global infO_product
    global type_texts
    types = call.data
    infO_product['Тип работы'] = type_texts[types]


def choise_order_deadline(call, bot):
    global infO_product
    global deadline_text
    category = call.data
    infO_product['Сроки'] = deadline_text[category][0]
    infO_product['Расчетная стоимость'] *= deadline_text[category][1]

def last_craete_order_message(call, bot):
    global infO_product
    message = f"""
    Ваш заказ:\n№ заказа - #1\nКатегория работы - {infO_product['Категория работы']}\nТип работы - {infO_product['Тип работы']}\nСроки - {infO_product['Сроки']}\nРасчетная стоимость - {infO_product['Расчетная стоимость']}\n\n*- Окончательная стоимость - (добавляется после подтверждения заказа у администратора)
    """
    bot.send_message(call.message.chat.id, text=message)





