from tkinter import *
from tkinter import font
from tkinter import ttk
from io import BytesIO
<<<<<<< HEAD
import urllib
import urllib.request
import folium
import webbrowser
from PIL import Image,ImageTk
=======
from PIL import ImageTk, Image

>>>>>>> a347e857add7a45c259aa0c80843e53490d6f994
from tour import *
from gmail import *
from kakaoMap import *

import requests


WIDTH = 900
HEIGHT = 450

class UI():
    def __init__(self):
        self.window = Tk()
        self.window.title("ReSCH")
        self.window.geometry(str(WIDTH)+'x'+str(HEIGHT))
        self.window.resizable(width=False , height = False)
        self.window.configure(bg="skyblue")
        self.fontstyle = font.Font(self.window, size=8, weight='bold', family='Consolas')

###############
        self.T = AreaCodeXML()
        self.areaCodeDict1 = self.T.makeAreaCode()
        self.areaCodeDict2 = {}
        self.B = AreaBasedList()
        ##################
        self.setupCombobox()
        self.setupButton()
        self.setupListbox()
        self.setupInfoMapFrame()




########################################################################################################################
        self.window.option_add('*TCombobox*Listbox.font', self.combofont)
        self.window.mainloop()

    # 왼쪽 Frame 리스트 박스 준비
    def setupListbox(self):
        frame = Frame(self.window,width=320,height=385,bg="gray")
        frame.place(x=10,y=50)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.adressfont = font.Font(frame, size=11, weight='bold', family='Consolas')
        self.adressList = Listbox(frame,selectmode ='browse',width=38,height = 20,font=self.adressfont,yscrollcommand = scrollbar.set, activestyle='none')
        scrollbar["command"] = self.adressList.yview
        self.adressList.pack(side=LEFT)

        self.adressList.bind("<Double-Button-1>", self.selectList)

    # 리스트에서 선택
    def selectList(self, *args):
        contentid = str(self.searchList[self.adressList.curselection()[0]][2])
<<<<<<< HEAD
        #print(str(contentid))
        self.mapx = float(makeDetail(contentid)["mapx"])
        self.mapy = float(makeDetail(contentid)["mapy"])

=======
        self.distroyInfoLabels()
        self.pressedInfo(makeDetail(contentid))
>>>>>>> a347e857add7a45c259aa0c80843e53490d6f994


    # 오른쪽 Frame 정보, 지도 그릴 Frame
    def setupInfoMapFrame(self):
        self.secondMyframe = Frame(self.window, relief=GROOVE, width=10, height=10, bg="white")
        self.secondMyframe.place(x=350, y=50)

        self.secondCanvas = Canvas(self.secondMyframe, width=450, height=380, bg="white")
        self.secondFrame = Frame(self.secondCanvas, bg="white")
        myscrollbar = Scrollbar(self.secondMyframe, orient="vertical", command=self.secondCanvas.yview)
        self.secondCanvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")

        self.secondCanvas.create_window((0, 0), window=self.secondFrame, anchor='nw')
        self.secondCanvas.pack(side="left")
        self.secondCanvas.create_window((0, 0), window=self.secondFrame, anchor='nw')
        self.secondFrame.bind("<Configure>", self.afterCanvasScroll)

    def afterCanvasScroll(self, event):
        self.secondCanvas.configure(scrollregion=self.secondCanvas.bbox("all"), width=450, height=380, bg="white")


    def distroyInfoLabels(self):
        for x in self.secondCanvas.find_all():
            self.secondCanvas.delete(x)

    # 버튼 설정
    def setupButton(self):
        # 검색 버튼
        self.searchfont = font.Font(self.window, size=11, weight='bold', family='Consolas')
        self.searchButton = Button(text="검색", width=5, height=1, font=self.searchfont, bg="white", fg="black",command=self.search)
        self.searchButton.place(x=430, y=10)

        # 정보 버튼
        self.infoImg = Image.open("img/info.png")
        self.infoImg = self.infoImg.resize((60,60), Image.ANTIALIAS)
        self.resizeInfoImg = ImageTk.PhotoImage(self.infoImg)
        self.infoTab = Button(self.window, width=60, height=60, bg="white", command=self.pressedInfo)
        self.infoTab["image"] = self.resizeInfoImg
        self.infoTab.place(x=820, y=50)

        # 지도 버튼
        self.mapImg = Image.open("img/map.png")
        self.mapImg = self.mapImg.resize((60,60), Image.ANTIALIAS)
        self.resizeMapImg = ImageTk.PhotoImage(self.mapImg)
        self.mapTab = Button(self.window, width=60, height=60, bg="white",command = self.pressedMap)
        self.mapTab["image"] = self.resizeMapImg
        self.mapTab.place(x=820, y=156)

        # 메일 보내기 버튼
        self.mailImg = Image.open("img/mail.png")
        self.mailImg = self.mailImg.resize((60,60), Image.ANTIALIAS)
        self.resizeMailImg = ImageTk.PhotoImage(self.mailImg)
        self.mailTab = Button(self.window, width=60, height=60, bg="white",command = Gmail())
        self.mailTab["image"] = self.resizeMailImg
        self.mailTab.place(x=820, y=262)

        # 챗봇 버튼튼
        self.chatbotImg = Image.open("img/chatbot.png")
        self.chatbotImg = self.chatbotImg.resize((60,60),Image.ANTIALIAS)
        self.resizeChatbotImg = ImageTk.PhotoImage(self.chatbotImg)
        self.chatbotTab = Button(self.window, width=60, height=60, bg="white")
        self.chatbotTab["image"] = self.resizeChatbotImg
        self.chatbotTab.place(x=820, y=430-62)


    # 콤보박스 (시/도), (시/군/구)
    def setupCombobox(self):
        self.combofont = font.Font(self.window, size=14, weight='bold', family='맑은 고딕')

        self.firstCombobox = ttk.Combobox(self.window, width=15,height=5, font=self.combofont)


        # 시/도 검색
        lst = [] #
        for value in self.areaCodeDict1.keys():
            lst.append(value)
        self.firstCombobox['values'] = tuple(lst)


        self.firstCombobox.set("시/도")
        self.firstCombobox.place(x=10, y=10)
        self.firstCombobox.configure(state='readonly')


        self.secondCombobox = ttk.Combobox(self.window, width=15, height=5, font=self.combofont)
        self.secondCombobox['values'] = ('')
        self.secondCombobox.set("시/군/구")
        self.secondCombobox.place(x=220, y=10)
        self.secondCombobox.configure(state='disabled')


        self.firstCombobox.bind("<<ComboboxSelected>>", self.firstComb_selected)

    def firstComb_selected(self, *args):
        if self.firstCombobox.current() != -1:
            self.secondCombobox.configure(state='readonly')
            self.T.setAreaCode(self.areaCodeDict1[self.firstCombobox.get()])
            self.areaCode = self.T.getAreaCode()
            self.areaCodeDict2 = self.T.makeAreaCode()
            lst = []
            for value in self.areaCodeDict2.keys():
                lst.append(value)
            self.secondCombobox['values'] = tuple(lst)
        if self.secondCombobox.current() == -1:
            self.secondCombobox.set("시/군/구")

    def search(self):
        self.sigunguCode = self.areaCodeDict2[self.secondCombobox.get()]
        self.areaCode = self.areaCodeDict1[self.firstCombobox.get()]
        self.B.setAreaCode(self.areaCode)
        self.B.setSigunguCode(self.sigunguCode)
        self.searchList = self.B.makeAreaBasedList()

        i = 0
        for l in self.searchList:
            self.adressList.insert(i, l[0])
            i+=1

    def pressedMap(self):
<<<<<<< HEAD

        m = folium.Map(location=[self.mapy, self.mapx],
                       tiles="OpenStreetMap", zoom_start=16)

        folium.Marker(location=[self.mapy, self.mapx],
                      icon=folium.Icon(color='red', icon='star', popup="ㅈ같다")).add_to(m)

        m.save("map.html")
        webbrowser.open_new('map.html')

=======
        self.distroyInfoLabels()


    def pressedInfo(self, d):
        print("dictionary")
        dictInfo = d
        Label(self.secondFrame, width=10, text="", bg="white").grid(row=0, column=0)
        Label(self.secondFrame, width=10, text="", bg="white").grid(row=0, column=2)
        i = 0
        LfirstImage = Label(self.secondFrame, bg='white')
        if 'title' in dictInfo:
            Label(self.secondFrame, text=dictInfo['title'], bg="white").grid(row=i, column=1)
            i += 1

        if 'firstimage' in dictInfo:
            img_url = dictInfo['firstimage']
            response = requests.get(img_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((300, 200), Image.ANTIALIAS)
            resizeImg = ImageTk.PhotoImage(img)
            LfirstImage['image'] = resizeImg
            LfirstImage.image = resizeImg
            LfirstImage.grid(row=i, column=1)
            i += 1
        else:
            Label(self.secondFrame, width=43, height=12, bg='gray').grid(row=i, column=1)
            i += 1

        if 'addr1' in dictInfo:
            Label(self.secondFrame, text="주소", bg="white", justify='left').grid(row=i, column=1)
            i += 2
            Label(self.secondFrame, text=dictInfo['addr1'] + "\n", bg="white", justify='left').grid(row=i, column=1)
            i += 2

        if 'tel' in dictInfo:
            Label(self.secondFrame, text="전화번호", bg="white", justify='left').grid(row=i, column=1)
            i += 2
            Label(self.secondFrame, text=dictInfo['tel'] + "\n", bg="white", justify='left').grid(row=i, column=1)
            i += 2

        if 'homepage' in dictInfo:
            Label(self.secondFrame, text="홈페이지", bg="white", justify='left').grid(row=i, column=1)
            i += 2

            str1 = dictInfo['homepage']
            str1 = str1.replace('\n', '')
            str = ""
            a = str1.find("<a")
            b = str1.find("a>")
            c = str1.find('href="')
            d = str1.find('" target')
            tempstr1 = str1[:a - 1]
            tempstr2 = str1[c + 6:d]
            str += tempstr1 + " - " + tempstr2 + "\n"
            for j in range(str1.count('<a') - 1):
                a = str1[a + 1:].find("<a") + a + 1
                tempstr1 = str1[b + 8:a - 1]
                b = str1[b + 8:].find("a>") + b + 8
                c = str1[c + 6:].find('href="') + c + 6
                d = str1[d + 8:].find('" target=') + d + 8
                tempstr2 = str1[c + 6:d]
                str += tempstr1 + " - " + tempstr2 + "\n"
            Label(self.secondFrame, text=str, bg="white", justify='left').grid(row=i, column=1)
            i += 2

        if 'zipcode' in dictInfo:
            Label(self.secondFrame, text="우편번호 - " + dictInfo['zipcode'] + "\n", bg="white", justify='left').grid(row=i, column=1)
            i += 2

        if 'overview' in dictInfo:
            Label(self.secondFrame, text="상세정보", bg="white", justify='left').grid(row=i, column=1)
            i += 2

            str = dictInfo['overview']

            a = str.find('*')
            str = str[a:]
            str = str.replace('<br>', '<br />')

            str1 = ""
            c = str.find('<br />')
            str1 += str[:c] + "\n"

            for j in range(str.count('<br />') - 1):
                str = str.replace(str[:c] + '<br />', '')
                c = str.find('<br />')
                str1 += str[:c] + "\n"

            Label(self.secondFrame, text=str1, bg="white", justify='left').grid(row=i, column=1)
>>>>>>> a347e857add7a45c259aa0c80843e53490d6f994


UI()

