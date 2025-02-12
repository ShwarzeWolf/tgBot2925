from telebot import TeleBot

from settings import TOKEN

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(
        message.chat.id,
        'Привет! Это бот показывания погоды, пока что находится в разработке.'
    )


bot.polling()
