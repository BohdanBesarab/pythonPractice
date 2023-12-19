import telebot
from telebot import types
import sqlite3


bot= telebot.TeleBot('6900126431:AAHTez4qsJIm5bcm5J8v7rgiTxfYtwVnYwc')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    #Open connect
    conn = sqlite3.connect('db_4les.sql')
    cur = conn.cursor()
    #create table with 3 parametres
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar (50),'
                ' pass varchar (50) )')
    conn.commit()
    #Close connect
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hello I want to regist you! Please set your name ')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Set your password ')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('db_4les.sql')
    cur = conn.cursor()
    # create table with 3 parametres
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s' , '%s' )" % (name, password))
    conn.commit()
    # Close connect
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('List of users', callback_data='users_list'))
    bot.send_message(message.chat.id, 'You were regist ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('db_4les.sql')
    cur = conn.cursor()
    # select from users
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, password: {el[2]}\n'
    # Close connect
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(none_stop=True)