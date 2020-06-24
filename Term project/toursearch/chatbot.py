#-*- coding:utf-8 -*-
#BDY_test_bot
#931618982:AAEQYTASmXoK9HItKMJSnaCiHC7XeuJbWHs
#1220588565 내 아이디

#api 토큰 SpWe9UpmMXVZh8MHhnRCpSeVMBO88OXs%2F%2FHIVBSWA3GLBFMhbV9i0WbynUMZ6G66WEUgerpPxoXEVU5DYrQRTg%3D%3D
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

import telepot
from telepot.loop import MessageLoop
import time

imgUrl = []
searchList = []

def chatbot():
    options = webdriver.ChromeOptions()

    # headless 옵션 설정
    options.add_argument('headless')
    options.add_argument("no-sandbox")

    # 브라우저 윈도우 사이즈
    options.add_argument('window-size=1920x1080')

    # 사람처럼 보이게 하는 옵션들
    options.add_argument("disable-gpu")  # 가속 사용 x
    options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

    TOKEN_MAIN = '931618982:AAEQYTASmXoK9HItKMJSnaCiHC7XeuJbWHs'  # 위에서 발급받은 토큰 기입

    def searchInChatbot(text):
        global searchList
        global imgUrl
        if imgUrl != None:
            imgUrl.clear()
        if searchList != None:
            searchList.clear()

        # 드라이버 위치 경로 입력

        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        driver.get('https://korean.visitkorea.or.kr/search/search_list.do?keyword=' + text + '&temp=')
        driver.implicitly_wait(3)  # 암묵적으로 웹 자원을 (최대) 3초 기다리기

        driver.find_element_by_xpath('//*[@id="tabView4"]/a').click()  # 여행지 클릭
        # driver.find_element_by_xpath('//*[@id="3"]').click()  # 인기순 클릭
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')  # BeautifulSoup사용하기

        li_index = 1

        spots = soup.select('#contents > div > div.box_leftType1 > ul > li >div.area_txt ')
        imgUrl = soup.find_all("img")

        for spot in spots:
            # name = spot.select_one('div > a').text()

            name_key = '//*[@id="contents"]/div/div[1]/ul/li[{index}]/div[2]/div/a'.format(index=li_index)
            address_key = '//*[@id="contents"]/div/div[1]/ul/li[{index}]/div[2]/p'.format(index=li_index)

            name = driver.find_element_by_xpath(name_key).text
            address = driver.find_element_by_xpath(address_key).text
            searchList.append({"name": name, "address": address})

            print("name", name, "address", address, "image", imgUrl)

            li_index = li_index + 1

        driver.close()

    def handle_main(msg):
        global searchList
        global imgUrl
        msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)

        print(msg)
        okheebot.sendMessage(chat_id, "검색하신 지명을 검색중입니다...")
        if msg_type == 'text':
            if msg['text'][0] == '!':
                searchString = msg['text'][1:]
                searchInChatbot(searchString)

                count = 0
                for list in searchList:
                    if imgUrl[count]['src'] != 'https://cdn.visitkorea.or.kr/img/call?cmd=VIEW&id=':
                        okheebot.sendPhoto(chat_id, imgUrl[count]['src'])

                    script = "\n명칭 : " + list['name'] + "\n"
                    script += "위치 : " + list['address'] + "\n\n"

                    okheebot.sendMessage(chat_id, script)
                    count += 1

        okheebot.sendMessage(chat_id, "검색하신 내용이 마음에 드시나요?")

    okheebot = telepot.Bot(TOKEN_MAIN)
    MessageLoop(okheebot, handle_main).run_as_thread()


