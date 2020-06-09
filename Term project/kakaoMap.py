import folium
from tkinter import *

window = Tk()
window.title("뻑")
window.geometry("500x500")
window.resizable(width=False , height = False)

canvas = Canvas(window)


m = folium.Map(location=[37.564214, 127.001699],
               tiles="OpenStreetMap",
               zoom_start=15)

canvas.create_bitmap(m)

folium.Marker(location=[37.564214, 127.001699],
              icon=folium.Icon(color='red', icon='star',
                               popup="Center of seoul")).add_to(m)

canvas.pack()

window.mainloop()