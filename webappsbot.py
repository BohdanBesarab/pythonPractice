from aiogram import  Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Open website', web_app=WebAppInfo(url = 'https://htmlpreview.github.io/?https://raw.githubusercontent.com/BohdanBesarab/pythonPractice/main/index.html')))
    await message.answer('Hello my friend', reply_markup=markup)

executor.start_polling(dp)