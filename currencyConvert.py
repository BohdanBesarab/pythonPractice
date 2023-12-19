import telebot
from currency_converter import CurrencyConverter
from telebot import types
bot = telebot.TeleBot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'Привіт. Введи суму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Невірний формат. Запишіть суму')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Інше значення', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Оберіть пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число повино бути більше за 0. Впишіть суму ')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Виходить : {round(res, 2)} Можете знову записати суму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Ведіть пару значень через слеш (/)')
        bot.register_next_step_handler(call.message, my_currancy)


def my_currancy (message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Виходить : {round(res, 2)} Можете знову записати суму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Щось пішло не так. Впишіть значення знову')
        bot.register_next_step_handler(message, my_currancy)



bot.polling(none_stop=True)