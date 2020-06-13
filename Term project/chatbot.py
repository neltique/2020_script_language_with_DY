from telegram.ext import *
from bs4 import BeautifulSoup
import requests

def show_music_rank(self, update):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    addr = 'https://www.melon.com/chart/index.html'
    self.addr = addr
    melon = requests.get(self.addr, headers=header)
    soup = BeautifulSoup(melon.text, 'html.parser')

    titles = soup.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
    artist = soup.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')
    update.message.reply_text('실시간 멜론 차트\n' + '1위: ' + titles[1].text + ' - ' + artist[1].text + '\n')

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="봇 작동합니다.")

def unknown(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="죄송하지만 그 명령어를 이해할 수 없습니다.")

def main():
    updater = Updater('931618982:AAEQYTASmXoK9HItKMJSnaCiHC7XeuJbWHs')
    dp = updater.dispatcher
    print("Bot started")

    updater.start_polling()
    dp.add_handler(CommandHandler('start',start))

    dp.add_handler(MessageHandler(Filters.command,unknown))

    updater.idle()



    dp.add_handler(CommandHandler('최신음악', show_music_rank))

    updater.stop()
if __name__ == '__main__':
    main()




