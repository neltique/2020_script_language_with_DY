import telegram
from chatbotModel import*

chii_token = '1029777872:AAHGPbSZZzcYQUlL6F-noUI29R4OaVLfH54'
chii = telegram.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message)