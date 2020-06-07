import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self,name,token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 1220588565
        self.name = name

    def sendMessage(self,text):
        self.core.sendMessage(chat_id = self.id,text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class MyBot(TelegramBot):
    def __init__(self):
        self.token = '1029777872:AAHGPbSZZzcYQUlL6F-noUI29R4OaVLfH54'
        TelegramBot.__init__(self,"도열",self.token)
        self.updater.stop()

    def add_handler(self,cmd,func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd,func))

    def start(self):
        self.sendMessage("봇이 작동을 시작합니다.")
        self.updater.start_polling()
        self.updater.idle()