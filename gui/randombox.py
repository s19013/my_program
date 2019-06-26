import tkinter as tk
from tkinter import messagebox as mbox
import random

def ok_click():
    s=textbox1.get()
    box=s.split()
    cou=textbox2.get()
    result["text"]=random.sample(box,int(cou))


#win
win = tk.Tk()
win.geometry("500x500")

#parts
#Label
setumei = tk.Label(win,text="名前を入れてね\n　ひとマス分開けて次の名前を入れてね")
setumei.place(x=125,y=2)
ninzuu=tk.Label(win,text="選び出す人数は？")
ninzuu.place(x=190,y=100)
result=tk.Label(win, text="")
result.place(x=215,y=200)
#textbox
textbox1 =tk.Entry(win, width=60)
textbox1.place(x=8,y=45)
textbox2 =tk.Entry(win, width=60)
textbox2.place(x=8,y=125)
#button
okButton = tk.Button(win, text='OK', command=ok_click)
okButton.place(x=215,y=160)
#------------------
win.mainloop()
