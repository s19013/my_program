import tkinter as tk
import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import font
import tkinter.ttk as ttk

win=tk.Tk()
win.geometry("600x600")

#フレーム
comside=tk.LabelFrame(win,bd=2,relief="ridge",text="相手",)
comside.pack(fill="x")
etcside=tk.Frame(win)
etcside.pack(fill="x")
myside=tk.LabelFrame(win,bd=2,relief="ridge",text="あなた",)
myside.pack(fill="x")
#部品
#-----------------------------
#関数
def game():
    yourcard=[]
    comcard=[]
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    lcomcard=tk.Label(comside,text=comcard)
    lcomcard.pack(side="left")
#実行
game()
win.mainloop()
