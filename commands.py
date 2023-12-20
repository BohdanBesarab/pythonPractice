import telebot
import webbrowser

bot = telebot.TeleBot('')
#створення команди на посилання на сайт
@bot.message_handler(commands=['site', 'website'])
def site (message):
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')


#  Створення 3 комнади і отрмати відповідь
@bot.message_handler(commands=['start', 'hello', 'main'])
def main (message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.username}')

# форматування тексту від бота
@bot.message_handler(commands='help')
def main (message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

# Вітання з особою через дані що містяться в message
@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'Your id is , {message.id}')
        bot.reply_to(message, f'ID : {message.from_user.id}')


bot.polling(none_stop=True)
