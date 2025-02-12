from telebot import TeleBot

from settings import TOKEN

bot = TeleBot(TOKEN)
bot.polling()
