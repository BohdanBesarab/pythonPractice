import telebot
from aiogram import Bot, Dispatcher, executor, types


bot = Bot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')
dp = Dispatcher(bot)


#@dp.message_handler(content_types=['text']) виключно на щось одне . Без контенту приймає все і функція старт працює
#@dp.message_handler(commands=['start'])
@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Привіт')
    #await message.answer('Привіт')
    await message.reply('Hello')

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site' , url= 'https://www.google.com/webhp?hl=uk&sa=X&ved=0ahUKEwiN0vmDh5qDAxWwPhAIHQ_iCWIQPAgJ'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)



@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message :types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)


executor.start_polling(dp)
#bot = telebot.TeleBot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')
#bot.polling(none_stop=True)