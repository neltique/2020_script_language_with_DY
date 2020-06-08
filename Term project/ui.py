from tkinter import *
from tkinter import font
from tkinter import ttk

from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
from tour import *
from gmail import *
from kakaoMap import *

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

        self.window.option_add('*TCombobox*Listbox.font', self.combofont)

        self.secondCanvas=Canvas(self.window, width = 450 , height = 380 ,bg="white" )
        self.secondCanvas.place(x=350, y=50)

########################################################################################################################

        self.window.mainloop()

    def setupListbox(self):
        frame = Frame(self.window,width=320,height=385,bg="gray")
        frame.place(x=10,y=50)

        scrollbar= Scrollbar(frame)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.adressfont = font.Font(frame, size=11, weight='bold', family='Consolas')
        self.adressList = Listbox(frame,selectmode ='browse',width=38,height = 20,font=self.adressfont,yscrollcommand = scrollbar.set, activestyle='none')
        scrollbar["command"] = self.adressList.yview



        self.adressList.pack(side=LEFT)
        self.adressList.bind("<Double-Button-1>", self.selectList)

    # 리스트에서 선택
    def selectList(self, *args):
        contentid = str(self.searchList[self.adressList.curselection()[0]][2])
        print(makeDetail(contentid)["mapx"],makeDetail(contentid)["mapy"])


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
        self.infoTab = Button(self.window, width=60, height=60, bg="white")
        self.infoTab["image"] = self.resizeInfoImg
        self.infoTab.place(x=820, y=50)

        # 지도 버튼
        self.mapImg = Image.open("img/map.png")
        self.mapImg = self.mapImg.resize((60,60), Image.ANTIALIAS)
        self.resizeMapImg = ImageTk.PhotoImage(self.mapImg)
        self.mapTab = Button(self.window, width=60, height=60, bg="white",command= self.pressedMap)
        self.mapTab["image"] = self.resizeMapImg
        self.mapTab.place(x=820, y=156)

        # 메일 보내기 버튼
        self.mailImg = Image.open("img/mail.png")
        self.mailImg = self.mailImg.resize((60,60), Image.ANTIALIAS)
        self.resizeMailImg = ImageTk.PhotoImage(self.mailImg)
        self.mailTab = Button(self.window, width=60, height=60, bg="white",command = Gmail() )
        self.mailTab["image"] = self.resizeMailImg
        self.mailTab.place(x=820, y=262)

        # 챗봇 버튼튼
        self.chatbotImg = Image.open("img/chatbot.png")
        self.chatbotImg = self.chatbotImg.resize((60,60),Image.ANTIALIAS)
        self.resizeChatbotImg = ImageTk.PhotoImage(self.chatbotImg)
        self.chatbotTab = Button(self.window, width=60, height=60, bg="white")
        self.chatbotTab["image"] = self.resizeChatbotImg
        self.chatbotTab.place(x=820, y=430-62)



# 콤보박스 (시/도), (시/군/구) #########XML
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
        pass


UI()

