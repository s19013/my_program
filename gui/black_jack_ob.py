import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk().title("Visualizer for function")
strfont=font.Font(size=25)
framefont=font.Font(size=16)


class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)
        #フレーム
        self.comside=tk.LabelFrame(win,bd=3,relief="groove",text="相手",font=framefont)
        self.comside.pack(fill="x")

        self.etcside=tk.Frame(win)
        self.etcside.pack(fill="x")

        self.yourside=tk.LabelFrame(win,bd=3,relief="groove",text="あなた",font=framefont)
        self.yourside.pack(fill="x")
        

class Card_base:
    def __init__(self,parson):
        self.parson=parson
        self.parsoncard=[]
        for i in range(2):
            self.parsoncard.append(random.randint(1,13))

    def hyouzi(self,parson):
        self.parson=parson
        self.parsoncard=tk.StringVar()
        self.parsoncard.set("{}".format(self.parsoncard))
        self.textparson_sum=tk.StringVar()
        self.textparson_sum.set("あなたの合計:{}".format(sum(self.parsoncard)))
        lmycord=tk.Label(yourside,font=strfont,textvariable=textmycard).pack(side"left")
        lmycord_sum=tk.Label(yourside,font=strfont,textvariable=textmycard_sum).pck(side="right")
