import telebot
import schedule
import time
from settings import TOKEN

def sending(bot):
    with open('database.txt') as db:
        number=db.read()
        bot.send_message(113079851, 'Осталось дней:' + number)
        number = int(number)
    with open('database.txt', 'w') as db:
        db.write((str(number-1)))

bot = telebot.TeleBot(TOKEN)

schedule.every(10).seconds.do(sending, bot)

while True:
    schedule.run_pending()
    time.sleep(1)
