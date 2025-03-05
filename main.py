import requests
from telebot import TeleBot

import settings

bot = TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(
        message.chat.id,
        'Привет! Это бот показывания погоды, пока что находится в разработке.'
    )


@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=40&lon=40&appid={settings.WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        bot.send_message(message.chat.id, weather)
    else:
        bot.send_message(message.chat.id, response.json()['message'])


bot.polling()
