import tkinter
import tkinter as tk
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk


win = tk.Tk()
win.title()
win.geometry("500x500")

class Card_base:
    def __init__(self,parson,parsoncard,Lparson,Lparsoncard_sum):
        self.parson=parson
        self.parsoncard=parsoncard
        self.parsoncard=[]
        self.Lparson=Lparson
        for i in range(2):
            self.parsoncard.append(random.randint(1,13))
        self.Lparsoncard_sum=Lparsoncard_sum
        self.Lparsoncard_sum=sum(self.parsoncard)
        #フォント
        self.strfont=font.Font(size=25)
        self.framefont=font.Font(size=16)
        #フレーム
        self.side=tk.LabelFrame(win,bd=3,relief="groove",text=self.parson,font=self.framefont)
        self.side.pack(fill="x")
        #表示
        Lparson=tk.Label(self.side,font=self.strfont,text="{0}".format(self.parsoncard)).pack(side="left")
        Lparsoncard=tk.Label(self.side,font=self.strfont,text="{0}".format(self.Lparsoncard_sum)).pack(side="right")


Card_base("you","yourcard","Lyou","Lyourcard_sum")
win.mainloop()
