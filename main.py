import os
import random
import telebot 
from telebot import types
from dotenv import load_dotenv
import requests
import json

load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
print(token)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Подписаться", url="https://github.com/elayLo")
    markup.add(btn)
    bot.send_message(message.from_user.id, "Привет, подпишись на мой GitHub", reply_markup=markup)
    bot.send_message(message.from_user.id, "Спасибо за поддержку, приятного использования")

@bot.message_handler(commands=["mars"])
def message_text(message):
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/photos?sol=531&api_key=DEMO_KEY")
    obj = response.json()
    picture = random.randrange(0, 10)
    img = obj["photos"][picture]["img_src"]
    bot.send_photo(message.from_user.id, img)

@bot.message_handler(commands=["iss"])
def message_text(message):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    obj = response.json()
    print(obj)
    lt = obj["iss_position"]["longitude"]
    lat = obj["iss_position"]["latitude"]
    bot.send_message(message.from_user.id, f"ISS position: longitude - {lt}, latitude - {lat}")


bot.polling(none_stop=True, interval=0)
