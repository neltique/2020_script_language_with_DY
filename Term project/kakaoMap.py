import urllib.request

from tkinter import *
from PIL import ImageTk, Image

import http.client
import xml.etree.ElementTree as ET
import urllib.request

def mapDownLoad(mapx, mapy):
     server = 'dapi.kakao.com'
     key = 'c11cd41a6b4ce614ae81b1b07cc954eb'  # 본인 카카오앱키 입력
     header = {'Authorization': 'KakaoAK '+key}


     conn = http.client.HTTPSConnection(server)
     conn.request("GET", "/v2/local/geo/transcoord.xml?x="+mapx+"&y="+mapy+"&input_coord=WGS84&output_coord=WCONGNAMUL", None, header)
     req = conn.getresponse()
     rb = req.read().decode('utf-8')
     print(rb)
     tree = ET.fromstring(rb)

     urlx = tree.find('documents/x').text
     urly = tree.find('documents/y').text

     for i in range(1, 16):
         url = 'https://ssl.daumcdn.net/map3/staticmap/image?srs=WCONGNAMUL&lv=' + str(i) + '&size=225x190&markers=symbol:sc_marker%7Clocation:' + urlx + ',' + urly
         urllib.request.urlretrieve(url, "maps/map" + str(i) + '.jpg')


root = Tk()
root.title("AVATAR")

root.geometry("900x450")

frame = Frame(root,background='white')
frame.place(x=350, y=50)
level = 4

canvas = Canvas(frame, width=450, height=380, bg="white",bd = 0, highlightthickness = 0)
canvas.pack()






def Image1(*args):
       global  level
       canvas.delete("all")
       if level<15:
         level += 1
       image1 = PhotoImage(file = "maps/map"+str(level)+".jpg")
       canvas.create_image(0,0,anchor='nw',image=image1)
       canvas.image = image1




def Image2(*args):
    global level
    canvas.delete("all")
    if level>1:
        level -= 1
    image1 = PhotoImage(file="maps/map" + str(level) + ".jpg")
    canvas.create_image(0, 0, anchor='nw', image=image1)
    canvas.image = image1


image1 = PhotoImage(file = "maps/map"+str(level)+".jpg")
canvas.create_image(0,0,anchor='nw',image=image1)

def MouseWheelHandler(event):
    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1
        return 1

    if delta(event)==1:
        Image1()
    else:
        Image2()

canvas.bind("<MouseWheel>", MouseWheelHandler)


zoomInCanvas = Canvas(frame, width=30, height=30, bg='gray',bd = 1, highlightthickness = 0)
zoomIn = ImageTk.PhotoImage(Image.open("img/zoomin.jpg"))  # PIL solution
zoomInCanvas.create_image(0,0,anchor='nw',image=zoomIn)
zoomInCanvas.place(x=450-32, y=380-64)
zoomInCanvas.bind("<Button-1>", Image2)




zoomOut = ImageTk.PhotoImage(Image.open("img/zoomOut.jpg"))  # PIL solution
zoomOutCanvas = Canvas(frame, width=30, height=30, bg='gray',bd = 1, highlightthickness = 0)
zoomOutCanvas.create_image(0,0,anchor='nw',image=zoomOut)
zoomOutCanvas.place(x=450-32, y=380-32)
zoomOutCanvas.bind("<Button-1>", Image1)


root.mainloop()
