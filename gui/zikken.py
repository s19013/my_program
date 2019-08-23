import tkinter as tk

win=tk.Tk()
win.geometry("500x500")
box=["aaaaa","bbbbbb","cccccc"]
class Label(tk.Label):
    def __init__(self,name):
        tk.Label.__init__(self,text=name)

for a in box:
    b=Label(a)
    b.pack()
win.mainloop()
