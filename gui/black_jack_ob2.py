import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk





class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("500x500")
        #フォント
        self.strfont=font.Font(size=25)
        self.framefont=font.Font(size=16)
        #フレーム
        self.comside=tk.LabelFrame(self,bd=3,relief="groove",text="相手",font=self.framefont)
        self.comside.pack(fill="x")

        self.etcside=tk.Frame(self)
        self.etcside.pack(fill="x")

        self.yourside=tk.LabelFrame(self,bd=3,relief="groove",text="あなた",font=self.framefont)
        self.yourside.pack(fill="x")
        #Card_base("you")


class Card_base:
    def __init__(self,parson):
        self.parson=parson
        self.parsoncard=[]
        for i in range(2):
            self.parsoncard.append(random.randint(1,13))
        self.hyouji("you")

    def hyouji(self,parson):
        self.parson=parson
        self.parsoncard=tk.StringVar()
        self.parsoncard.set("{}".format(self.parsoncard))
        self.textparson_sum=tk.StringVar()
        self.textparson_sum.set("あなたの合計:{}".format(sum(self.parsoncard)))
        lmycord=tk.Label(self.yourside,font=self.strfont,textvariable=self.textmycard).pack(side="left")
        lmycord_sum=tk.Label(self.yourside,font=self.strfont,textvariable=self.textmycard_sum).pck(side="right")
def main():
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

main()