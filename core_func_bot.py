import telebot
from telebot import types

bot = telebot.TeleBot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')


@bot.message_handler(commands=['start'])
def start(message):
    #cтворення кнопок KeyboardButton видовжені і в тексті row новий рядок
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(' Move to site')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Edit text')
    markup.row(btn2, btn3)
    file= open('Photo1.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup )
    #bot.send_message(message.chat.id, 'Helloooo' , reply_markup=markup)

    bot.register_next_step_handler(message, on_click)
    #створення функції що буде після натискання
def on_click(message):
    if message.text == 'Move to site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id,'Deleted')





# Створення кнопок але в іншому виглідя (під повідомленням) через add добавляє в стовбець
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1= types.InlineKeyboardButton('Move to site', url='https://www.google.com/webhp?hl=uk&sa=X&ved=0ahUKEwirwPmQs5eDAxUXGxAIHSZYDTQQPAgJ')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data= 'delete' )
    btn3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'This photo is so cute!', reply_markup = markup)

# Посилаємось на дію після натискання на кнопку
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id )


bot.polling(none_stop=True)