# -*- coding: utf-8 -*-


#import webbrowser

#url = 'http://blindfish.tistory.com'

#webbrowser.open(url)





################################################################
from tkinter import *
from tkinter import font
from tkinter import ttk
from io import BytesIO
from PIL import ImageTk, Image

import requests
import tour

from bs4 import BeautifulSoup



dic = tour.makeDetail('126508')

def data(random):
    Label(frame, width=10, text="", bg="white").grid(row=0, column=0)
    Label(frame, width=10, text="", bg="white").grid(row=0, column=2)

    i=0
    LfirstImage = Label(frame, bg='white')
    if 'title' in random:
        Label(frame, text=random['title'], bg="white").grid(row = i, column = 1)
        i+=1

    if 'firstimage' in random:
        img_url = random['firstimage']
        response = requests.get(img_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 200), Image.ANTIALIAS)
        resizeImg = ImageTk.PhotoImage(img)
        LfirstImage['image'] = resizeImg
        LfirstImage.image = resizeImg
        LfirstImage.grid(row=i, column=1)
        i+=1
    else:
        Label(frame, width = 43, height = 12, bg = 'gray').grid(row=i,column=1)
        i += 1

    if 'addr1' in random:
        Label(frame, text="주소", bg="white", justify='left').grid(row=i, column=1)
        i += 2
        Label(frame, text= random['addr1']+"\n", bg="white",justify = 'left').grid(row=i, column=1)
        i += 2

    if 'tel' in random:
        Label(frame, text="전화번호", bg="white", justify='left').grid(row=i, column=1)
        i += 2
        Label(frame, text= random['tel']+"\n", bg="white",justify = 'left').grid(row=i, column=1)
        i += 2

    if 'homepage' in random:
        Label(frame, text="홈페이지", bg="white", justify='left').grid(row=i, column=1)
        i+=2

        str1 = random['homepage']
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
            str += tempstr1 + " - " + tempstr2+"\n"
        Label(frame, text=str, bg="white",justify = 'left').grid(row=i, column=1)
        i += 2

    if 'zipcode' in random:
        Label(frame, text="우편번호 - " + random['zipcode']+"\n", bg="white",justify = 'left').grid(row=i, column=1)
        i += 2

    if 'overview' in random:
        Label(frame, text="상세정보", bg="white", justify='left').grid(row=i, column=1)
        i += 2

        str = random['overview']

        a = str.find('*')
        str = str[a:]
        print(str)
        str = str.replace('<br>', '<br />')

        str1 = ""
        c = str.find('<br />')
        str1 += str[:c] + "\n"

        for j in range(str.count('<br />')-1):
            str = str.replace(str[:c] + '<br />', '')
            c = str.find('<br />')
            str1 += str[:c] + "\n"

        Label(frame, text=str1, bg="white",justify = 'left').grid(row=i, column=1)






def afterCanvasScroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=450,height=380,bg="white")

window = Tk()
window.geometry("900x450")
window.resizable(width=False, height=False)
window.configure(bg="skyblue")



myframe=Frame(window,relief=GROOVE,width=10,height=10,bg = "white")
myframe.place(x=350, y=50)

canvas=Canvas(myframe,width=450, height=380, bg="white")
frame=Frame(canvas,bg="white")
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")

canvas.create_window((0,0),window=frame,anchor='nw')
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>", afterCanvasScroll)

data(dic)





window.mainloop()


