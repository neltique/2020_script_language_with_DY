from tkinter import *
from tkinter import font

width = 900
height = 500
def UI():
    window = Tk()
    window.title("테스트")
    window.geometry('900x500')
    window.configure(bg="skyblue")
    window.resizable(True,True)
    fontstyle = font.Font(window, size=8, weight='bold', family='Consolas')


    listcanvas = Canvas(window, width = 300 , height = 430 ,bg="white" )
    listcanvas.place(x=10,y=50)

    secondCanvas=Canvas(window, width = 450 , height = 430 ,bg="white" )
    secondCanvas.place(x=350, y=50)

##########################################################################
    firstTab = Canvas(window, width=60, height=70, bg="white")
    firstTab.place(x=820, y=50)

    secondTab = Canvas(window, width=60, height=70, bg="white")
    secondTab.place(x=820, y=150)

    thirdTab = Canvas(window, width=60, height=70, bg="white")
    thirdTab.place(x=820, y=250)

    forthTab = Canvas(window, width=60, height=70, bg="white")
    forthTab.place(x=820, y=350)
############################################################################
#검색 entry:string을 받아 검색 button 누르면 string 읽어오기
    filename = StringVar()
    entry1 = Entry(window, width=15, textvariable=filename)
    entry1.place(x=270, y=10)

    filename2 = StringVar()
    entry2 = Entry(window, width=15, textvariable=filename2)
    entry2.place(x=400, y=10)

#글씨
    search = Button(text="검색",width = 3 ,height= 1 ,font=fontstyle ,bg="white",fg="black")
    search.place(x=530,y=10)


    window.mainloop()

UI()

