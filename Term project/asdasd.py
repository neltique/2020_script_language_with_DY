from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")
month = StringVar()
combobox1 = ttk.Combobox(root, textvariable = month)
combobox1.config(values = ('Jan', 'Feb', 'August'))
combobox1.pack()
date = StringVar()
global comb2

comb2 = ttk.Combobox(root, textvariable = date)
comb2.pack()
comb2.config(state=DISABLED)

def comb1_selected(*args):
    if (combobox1.current() != -1 ):
        comb2.config(state='normal')
        if combobox1.get() == 'Jan':
            comb2.config(values=('J'))

combobox1.bind("<<ComboboxSelected>>", comb1_selected)
root.mainloop()