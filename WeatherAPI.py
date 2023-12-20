import telebot
import requests
import json

bot = telebot.TeleBot('')
API = '4ae0063d54d0c91af1de1419276d79c6'

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'Glad to see you. Please set your sity' )


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code ==200:
        data = json.loads(res. text)
        temp=data["main"]["temp"]
        weath= data['weather'][0]['main']
        bot.reply_to(message, f'Now temperature : {temp}\n Out of window : {weath}' )

        image = 'sun.jpg' if temp > 5.0 else 'sunwithclouds.jpg'
        file= open('./' + image, 'rb' )
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'City not found')





bot.polling(none_stop=True)
