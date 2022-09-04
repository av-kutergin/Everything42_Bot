import os

import telebot
from telebot import types
from dotenv import load_dotenv
load_dotenv()

TG_TOKEN = os.environ["TG_TOKEN"]

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=["letssavephoto"])
def get_new_image(message):
    bot.send_message(message.chat.id, "Ready to save")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Hi, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Nice", parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Web", url="pikabu.ru"))
    bot.send_message(message.chat.id, "Go to site", reply_markup=markup)


@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Web')
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Go to site", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello to you", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id is {message.from_user.id}", parse_mode='html')
    elif message.text == "cheatsheet":
        photo = open("cheatsheet.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "I dont understand", parse_mode='html')


bot.infinity_polling()
# bot.polling(none_stop=True)
