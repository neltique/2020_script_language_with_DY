from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tkinter import *
from tkinterhtml import *
from tkinter import font
from tkinter import messagebox
from urllib.request import urlopen
from PIL import ImageTk, Image

from toursearch.tourData import *

import smtplib
import webbrowser
import io
import json
import spam

from toursearch import chatbot, kakaoMap, dictToHTML

with open('AreaCodes.json', 'r', encoding='UTF-8-sig') as f:
     AreaCodeData = json.load(f)


WIDTH = 900
HEIGHT = 450


def gantihal(frame):
    frame.tkraise()

class TourSearchGUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("ReSCH")
        self.window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        self.window.resizable(width=False, height=False)
        self.window.configure(bg="skyblue")
        self.fontstyle = font.Font(self.window, size=8, weight='bold', family='Consolas')
        self.timeFontStyle = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.infoCount = 0
        self.mapLevel = 5

        self.possiblemail = False

        ###############
        self.areaCodeDict = AreaCodeData        # json파일로 지역 dict를 받아온다
        self.AreaBasedList = AreaBasedList()    # api로 리스트 준비
        ##################
        self.setupCombobox()
        self.setupButton()
        self.setupListbox()


        self.setupInfoMapFrame()
        self.spam()
        ########################################################################################################################
        self.window.option_add('*TCombobox*Listbox.font', self.combofont)
        self.window.mainloop()

    # 왼쪽 Frame 리스트 박스 준비
    def setupListbox(self):
        firstFrame = Frame(self.window, width=320, height=385, bg="gray",bd = 0, highlightthickness = 0)
        firstFrame.place(x=10, y=50)

        scrollbar = Scrollbar(firstFrame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.adressfont = font.Font(firstFrame, size=11, weight='bold', family='Consolas')
        self.adressList = Listbox(firstFrame, selectmode='browse', width=38, height=20, font=self.adressfont,
                                  yscrollcommand=scrollbar.set, activestyle='none',bd = 0, highlightthickness = 0)
        scrollbar["command"] = self.adressList.yview
        self.adressList.pack(side=LEFT)

        self.adressList.bind("<Double-Button-1>", self.selectListDouble)

    # 리스트 더블 클릭
    def selectListDouble(self, *args):
        self.infoCount = 0
        self.makeInfoDetailDict()
        self.makeInfoFrame()
        kakaoMap.mapDownLoad(self.mapx, self.mapy)
        self.mapLevel = 5
        self.makeMapFrame()

    # 맵 다운로드, 정보 가져오는 함수
    def makeInfoDetailDict(self):
        # 선택된 리스트의 contentid 값을 가져와 dictionary에 저장, x좌표와 y 좌표를 저장
        contentid = str(self.searchList[self.adressList.curselection()[0]][2])
        self.infoDict = makeDetail(contentid)
        self.mapx = self.infoDict["mapx"]
        self.mapy = self.infoDict["mapy"]
        self.possiblemail = True

    # 오른쪽 Frame 정보, 지도 그릴 Frame
    def setupInfoMapFrame(self):
        self.MapFrame = Frame(self.window, relief=GROOVE, width=100, height=10, bg="white", bd=0, highlightthickness=0)
        self.MapFrame.place(x=350, y=50)
        self.MapCanvas = Canvas(self.MapFrame, width=450, height=380, bg="white", bd=0, highlightthickness=0)
        self.MapCanvas.pack()

        self.InfoFrame = Frame(self.window, relief=GROOVE, width=450, height=380, bg="white", bd=0, highlightthickness=0)
        self.InfoFrame.place(x=350, y=50)
        self.InfoFrame.propagate(0)
        self.InfoCanvasFrame = HtmlFrame(self.InfoFrame, fontscale=1, horizontal_scrollbar=False, vertical_scrollbar=False)
        self.InfoCanvasFrame.pack()


    # 버튼 설정
    def setupButton(self):
        # 검색 버튼
        self.searchfont = font.Font(self.window, size=11, weight='bold', family='Consolas')
        self.searchButton = Button(text="검색", width=5, height=1, font=self.searchfont, bg="white", fg="black",
                                   command=self.search)
        self.searchButton.place(x=430, y=10)

        # 정보 버튼
        self.infoImg = Image.open("../img/info.png")
        self.infoImg = self.infoImg.resize((60, 60), Image.ANTIALIAS)
        self.resizeInfoImg = ImageTk.PhotoImage(self.infoImg)
        self.infoTab = Button(self.window, width=60, height=60, bg="white",bd = 0,highlightthickness = 0, command=lambda:gantihal(self.InfoFrame))
        self.infoTab["image"] = self.resizeInfoImg
        self.infoTab.place(x=830, y=50)

        # 지도 버튼
        self.mapImg = Image.open("../img/map.png")
        self.mapImg = self.mapImg.resize((60, 60), Image.ANTIALIAS)
        self.resizeMapImg = ImageTk.PhotoImage(self.mapImg)
        self.mapTab = Button(self.window, width=60, height=60, bg="white",bd = 0,highlightthickness = 0, command=lambda:gantihal(self.MapFrame))
        self.mapTab["image"] = self.resizeMapImg
        self.mapTab.place(x=830, y=156)

        # 메일 보내기 버튼
        self.mailImg = Image.open("../img/mail.png")
        self.mailImg = self.mailImg.resize((60, 60), Image.ANTIALIAS)
        self.resizeMailImg = ImageTk.PhotoImage(self.mailImg)
        self.mailTab = Button(self.window, width=60, height=60, bg="white",bd = 0,highlightthickness = 0, command= self.Gmail)
        self.mailTab["image"] = self.resizeMailImg
        self.mailTab.place(x=830, y=262)

        # 챗봇 버튼튼
        self.chatbotImg = Image.open("../img/chatbot.png")
        self.chatbotImg = self.chatbotImg.resize((60, 60), Image.ANTIALIAS)
        self.resizeChatbotImg = ImageTk.PhotoImage(self.chatbotImg)
        self.chatbotTab = Button(self.window, width=60, height=60,bd = 0,highlightthickness = 0, bg="white",command=self.pressedChatbot)
        self.chatbotTab["image"] = self.resizeChatbotImg
        self.chatbotTab.place(x=830, y=430 - 62)

    # 콤보박스 (시/도), (시/군/구)
    def setupCombobox(self):
        self.combofont = font.Font(self.window, size=14, weight='bold', family='맑은 고딕')
        self.firstCombobox = ttk.Combobox(self.window, width=15, height=5, font=self.combofont)

        # 시/도 검색
        lst = []  #
        for key in self.areaCodeDict.keys():
            lst.append(key)
        self.firstCombobox['values'] = lst

        self.firstCombobox.set("시/도")
        self.firstCombobox.place(x=10, y=10)
        self.firstCombobox.configure(state='readonly')

        self.secondCombobox = ttk.Combobox(self.window, width=15, height=5, font=self.combofont)
        self.secondCombobox['values'] = ('')
        self.secondCombobox.set("시/군/구")
        self.secondCombobox.place(x=220, y=10)
        self.secondCombobox.configure(state='disabled')

        self.firstCombobox.bind("<<ComboboxSelected>>", self.firstComb_selected)
        self.firstCombobox.bind("<Button-1>",self.firstCombName_selectd)

    def firstCombName_selectd(self, *args):
        self.secondCombobox.configure(state = 'disabled')
        self.secondCombobox.set("시/군/구")

    def firstComb_selected(self, *args):
        if self.firstCombobox.current() != -1:
            self.secondCombobox.configure(state='readonly')
            # 시/군/구 검색
            lst = []
            for key in self.areaCodeDict[self.firstCombobox.get()]["AreaCode"]:
                lst.append(key)
            self.secondCombobox['value'] = lst



    def search(self):
        if self.secondCombobox.current() != -1:
            self.adressList.delete(0,END)
            self.sigunguCode = self.areaCodeDict[self.firstCombobox.get()]["AreaCode"][self.secondCombobox.get()]
            self.areaCode = self.areaCodeDict[self.firstCombobox.get()]["Code"]

            self.AreaBasedList.setAreaCode(self.areaCode)
            self.AreaBasedList.setSigunguCode(self.sigunguCode)
            self.searchList = self.AreaBasedList.makeAreaBasedList()

            for l in self.searchList:
                self.adressList.insert(END, l[0])
        else:
            print("You did not select area")

    # 수정해야함
    def makeInfoFrame(self):
        images = {}

        def renderimage(url):
            fp = urlopen(url)
            data = fp.read()
            fp.close()
            image = Image.open(io.BytesIO(data))
            photo = ImageTk.PhotoImage(image)
            images[url] = photo
            return photo

        self.InfoCanvas = TkinterHtml(self.InfoCanvasFrame, fontscale=0.8, imagecmd=renderimage)
        self.InfoCanvas.grid(row=0, column=0, sticky=tk.NSEW)

        vsb = ttk.Scrollbar(self.InfoCanvasFrame, orient=tk.VERTICAL, command=self.InfoCanvas.yview)
        self.InfoCanvas.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky=tk.NSEW)

        self.InfoCanvas.reset()
        self.InfoCanvas.parse(dictToHTML.dictToHTML(self.infoDict))





    # 지도 완성, 지도 이미지 다운 받는 부분 속도가 느림
    def makeMapFrame(self):
        mapImage = PhotoImage(file="maps/map" + str(self.mapLevel) + ".jpg")
        self.MapCanvas.create_image(0,0,anchor='nw', image=mapImage)
        self.MapCanvas.image = mapImage
        self.MapCanvas.bind("<MouseWheel>", self.MouseWheelHandlerInMap)

        zoomInCanvas = Canvas(self.MapFrame, width=30, height=30, bg='gray', bd=1, highlightthickness=0)
        zoomIn = ImageTk.PhotoImage(Image.open("../img/zoomIn.jpg"))  # PIL solution
        zoomInCanvas.create_image(0, 0, anchor='nw', image=zoomIn)
        zoomInCanvas.image = zoomIn
        zoomInCanvas.place(x=450 - 32, y=380 - 64)
        zoomInCanvas.bind("<Button-1>", self.zoomInMap)

        zoomOut = ImageTk.PhotoImage(Image.open("../img/zoomOut.jpg"))  # PIL solution
        zoomOutCanvas = Canvas(self.MapFrame, width=30, height=30, bg='gray', bd=1, highlightthickness=0)
        zoomOutCanvas.create_image(0, 0, anchor='nw', image=zoomOut)
        zoomOutCanvas.image = zoomOut
        zoomOutCanvas.place(x=450 - 32, y=380 - 32)
        zoomOutCanvas.bind("<Button-1>", self.zoomOutMap)

    def zoomOutMap(self, *args):
        self.MapCanvas.delete("all")
        if self.mapLevel < 15:
            self.mapLevel += 1
        mapImage = PhotoImage(file="maps/map" + str(self.mapLevel) + ".jpg")
        self.MapCanvas.create_image(0, 0, anchor='nw', image=mapImage)
        self.MapCanvas.image = mapImage

    def zoomInMap(self, *args):
        self.MapCanvas.delete("all")
        if self.mapLevel > 1:
            self.mapLevel -= 1
        mapImage = PhotoImage(file="maps/map" + str(self.mapLevel) + ".jpg")
        self.MapCanvas.create_image(0, 0, anchor='nw', image=mapImage)
        self.MapCanvas.image = mapImage

    def MouseWheelHandlerInMap(self,event):
        def delta(event):
            if event.num == 5 or event.delta < 0:
                return -1
            return 1
        if delta(event) ==1:
            self.zoomInMap()
        else:
            self.zoomOutMap()

    def send_mail(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('qorehduf3@gmail.com', 'jvljgoaecwgljjxe')

        msg = MIMEMultipart()
        msg['Subject'] = "요청하신 관광지 정보입니다."

        part = MIMEText(dictToHTML.dictToHTML(self.infoDict), 'html')
        msg.attach(part)

        s.sendmail("qorehduf3@gmail.com", self.entry_formula_input.get(), msg.as_string())

        s.quit()

        messagebox.showinfo("메일 보내기 완료", "현재 선택한 관광지 정보를 \n"+self.entry_formula_input.get()+"로 송신을 완료했습니다.")

        self.widget.destroy()


    def Gmail(self):
        if self.possiblemail == True:
            self.widget = Tk()
            self.widget.title("보낼 E-MAIL 입력")
            self.widget.geometry("300x100")


            self.entry_formula_input = Entry(self.widget,width=40,justify='left')
            self.entry_formula_input.place(x=10,y=5)

            self.inputmailvar = StringVar()

            self.sendbuttonfont = font.Font(self.widget, size=10, weight='bold', family='Consolas')
            sendbutton = Button(self.widget,text="send",width=30,height=3,font=self.sendbuttonfont,command=self.send_mail)


            sendbutton.place(x=30,y=30)

            self.widget.mainloop()
        else:
            messagebox.showwarning("메일 보내기 실패!", "보낼 관광지 정보가 없습니다.\n메일을 보내려면 관광지를 선택해주시기 바랍니다.")

    def pressedChatbot(self):
        webbrowser.open_new('https://web.telegram.org/#/im?p=@BDY_test_bot')
        chatbot.chatbot()

    def spam(self):
        a = spam.strlen('dd')
        time = Label(self.window, width = 30,font = self.timeFontStyle, text = "프로그램 시작 시간 - "+str(a[0])+"시 "+str(a[1])+"분", fg = "black", bg="skyblue" )
        time.place(x=550,y=10)












        


TourSearchGUI()