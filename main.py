import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['getdays'])

def getdays(message):
    with open('database.txt') as db:
        bot.send_message(message.chat.id, db.read())


if __name__ =='__main__':
    bot.polling(none_stop=True)