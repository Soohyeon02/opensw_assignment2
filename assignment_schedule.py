import telegram
import schedule
import time
import pytz
import datetime
import asyncio

# Bot : hmhgmg_bot
# token : 6406680094:AAG_QZZ5zhy54y8y8vt3wkEYQ82ePPpsBH8
# chat_id: 6585985233
# channel : hmhgmg_test

def job():
  
  token = "6406680094:AAG_QZZ5zhy54y8y8vt3wkEYQ82ePPpsBH8"
  bot = telegram.Bot(token=token)
  chat_id = "6585985233"
  text = "alarm arrived!!!!!"

  now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
  if now.hour >= 23 or now.hour <= 6:
    return

  asyncio.run(bot.sendMessage(chat_id = chat_id, text=text))

job()
schedule.every(30).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(30)  