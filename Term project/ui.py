from tkinter import *
from tkinter import font
from tkinter import ttk

from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
from tour import *

WIDTH = 900
HEIGHT = 450

class UI():
    def __init__(self):
        self.window = Tk()
        self.window.title("ReSCH")
        self.window.geometry(str(WIDTH)+'x'+str(HEIGHT))
        self.window.configure(bg="skyblue")
        self.window.resizable(True,True)
        self.fontstyle = font.Font(self.window, size=8, weight='bold', family='Consolas')
###############
        self.T = tour()
        self.areaCodeDict1 = self.T.makeAreaCode()
        self.areaCodeDict2 = {}
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
        #self.listCanvas = Canvas(self.window, width = 300 , height = 385 ,bg="white" )
        #self.listCanvas.place(x=10,y=50)

        self.adressfont = font.Font(self.window, size=11, weight='bold', family='Consolas')
        self.adressList = Listbox(self.window,selectmode='extended', height=20)
        self.adressList['width'] = 40
        self.adressList['font'] = self.adressfont
        self.adressList['activestyle']='none'

        ###########XML###########
        self.adressList.insert(0, "경기도 시흥시 정왕동 1호")
        self.adressList.insert(1, "경기도 시흥시 정왕동 2호")
        self.adressList.insert(3, "경기도 시흥시 정왕동 3호")
        self.adressList.insert(4, "경기도 시흥시 정왕동 4호")
        self.adressList.insert(5, "경기도 시흥시 정왕동 5호")
        self.adressList.insert(6, "경기도 시흥시 정왕동 6호")

        self.adressList.place(x=10,y=50)


# 버튼 설정
    def setupButton(self):
        # 검색 버튼
        self.searchfont = font.Font(self.window, size=11, weight='bold', family='Consolas')
        self.searchButton = Button(text="검색", width=5, height=1, font=self.searchfont, bg="white", fg="black",command=self.search)
        self.searchButton.place(x=430, y=10)

        # 취소 버튼

        self.undoImg = Image.open("img/undo.png")
        self.undoImg = self.undoImg.resize((25,25),Image.ANTIALIAS)
        self.resizeUndoImg = ImageTk.PhotoImage(self.undoImg)

        self.undoButton = Button(self.window, width=27, height=27, bg="white", command=self.undo)
        self.undoButton["image"] = self.resizeUndoImg
        self.undoButton.place(x=500, y=10)

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
        self.mapTab = Button(self.window, width=60, height=60, bg="white")
        self.mapTab["image"] = self.resizeMapImg
        self.mapTab.place(x=820, y=156)

        # 메일 보내기 버튼
        self.mailImg = Image.open("img/mail.png")
        self.mailImg = self.mailImg.resize((60,60), Image.ANTIALIAS)
        self.resizeMailImg = ImageTk.PhotoImage(self.mailImg)
        self.mailTab = Button(self.window, width=60, height=60, bg="white")
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

        lst = []
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
        self.secondCombobox.configure(state='readonly')
        self.secondCombobox.config(state = DISABLED)

        self.firstCombobox.bind("<<ComboboxSelected>>", self.firstComb_selected)

    def firstComb_selected(self, *args):
        if self.firstCombobox.current() != -1:
            self.secondCombobox.config(state='normal')
            self.T.setAreaCode(self.areaCodeDict1[self.firstCombobox.get()])
            self.areaCodeDict2 = self.T.makeAreaCode()
            lst = []
            for value in self.areaCodeDict2.keys():
                lst.append(value)
            self.secondCombobox['values'] = tuple(lst)


    def search(self):
        pass

    def undo(self):
        pass

UI()

