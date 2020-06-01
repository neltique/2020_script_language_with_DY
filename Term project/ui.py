from tkinter import *
from tkinter import font

width = 900
height = 500
def UI():
    window = Tk()
    window.title("테스트")
    window.geometry('900x500')
    window.configure(bg="skyblue")


    listcanvas = Canvas(window, width = 300 , height = 430 ,bg="white" )
    listcanvas.place(x=10,y=50)


#검색 entry:string을 받아 검색 button 누르면 string 읽어오기
    filename = StringVar()
    entry1 = Entry(window, width=20, textvariable=filename)
    entry1.place(x=200, y=10)

    filename2 = StringVar()
    entry2 = Entry(window, width=20, textvariable=filename2)
    entry2.place(x=400, y=10)




    window.mainloop()

UI()

