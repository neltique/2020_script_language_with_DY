# -*- coding: euc-kr -*-

#BDY_test_bot
#931618982:AAEQYTASmXoK9HItKMJSnaCiHC7XeuJbWHs
#1220588565 내 아이디
#api 토큰 SpWe9UpmMXVZh8MHhnRCpSeVMBO88OXs%2F%2FHIVBSWA3GLBFMhbV9i0WbynUMZ6G66WEUgerpPxoXEVU5DYrQRTg%3D%3D

from bs4 import BeautifulSoup
from urllib import parse
from collections import OrderedDict #중복 제거
import requests
import os
import telegram

def Site_ON():
    search = parse.urlparse('https://www.boannews.com/search/news_list.asp?search=title&find=취약점')
    query = parse.parse_qs(search.query) #보안뉴스 인코딩 값이 euc-kr
    S_query = parse.urlencode(query, encoding='euc-kr', doseq=True) # URL 인코딩
    url = "https://www.boannews.com/search/news_list.asp?{}".format(S_query)
    Article_Crawll(url)

def Article_Crawll(url):
    news_link = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        notices_link = link['href']
        if '/media/view.asp?idx=' in notices_link:
            news_link.append(notices_link) #news_link에 리스트 추가

    news_link = list(OrderedDict.fromkeys(news_link)) #중복제거
    Compare(news_link)

def Compare(news_link):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    temp = []
    cnt = 0
    with open(os.path.join(BASE_DIR, 'compare.txt'), 'r')as f_read:
        before = f_read.readlines()
        before = [line.rstrip() for line in before] #(\n)strip in list

        f_read.close()
        for i in news_link:
            if i not in before:
                temp.append(i)
                cnt = cnt + 1
                with open(os.path.join(BASE_DIR, 'compare.txt'), 'a') as f_write:
                    f_write.write(i+'\n')
                    f_write.close()
        if cnt > 0: #cnt가 1이라도 증가하면 새로운 기사가 있다는 뜻
            Maintext_Crawll(temp, cnt)

def Maintext_Crawll(temp, cnt):
    bot = telegram.Bot(token='931618982:AAEQYTASmXoK9HItKMJSnaCiHC7XeuJbWHs')
    chat_id = bot.getUpdates()[-1].message.chat.id
    NEW = "[+] 보안뉴스 ' 취약점 '에 새로운 뉴스는 {}개 입니다.".format(cnt)
    bot.sendMessage(chat_id=chat_id, text=NEW)
    for n in temp:
        Main_URL = "https://www.boannews.com{}".format (n.strip())
        bot.sendMessage(chat_id=chat_id, text=Main_URL)

        response = requests.get(Main_URL)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all("div",{"id":"news_title02"})
        contents = soup.find_all("div",{"id":"news_content"})
        date = soup.find_all("div",{"id":"news_util01"})
        photos = soup.find_all("div",{"class":"news_image"})
        for n in contents:
            text = n.text.strip()

if __name__ == "__main__":
    Site_ON()

