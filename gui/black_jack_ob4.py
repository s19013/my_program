import tkinter
import tkinter as tk
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk





class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("500x500")
        Card_base("you","yourcard","Lyou","Lyourcard")


class Card_base:
    def __init__(self,parson,parsoncard,Lparson,Lparsoncard):
        self.parson=parson
        self.parsoncard=parsoncard
        self.Lparson=Lparson
        self.Lparsoncard=Lparsoncard
        parsoncard=[]
        for i in range(2):
            parsoncard.append(random.randint(1,13))
        #フォント
        self.strfont=font.Font(size=25)
        self.framefont=font.Font(size=16)
        #フレーム
        self.side=tk.LabelFrame(self,bd=3,relief="groove",text=self.parson,font=("self.framefont"))
        self.side.pack(fill="x")
        #表示
        Lparson=tk.Label(self.side,font=("strfont"),textvariable=self.textmycard).pack(side="left")
        Lparsoncard=tk.Label(self.side,font=("strfont"),textvariable=self.textmycard_sum).pack(side="right")

def main():
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

main()
