import Tkinter
import tkinter as tk
import random
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time

win=tk.Tk()
win.geometry("600x600")
#フォント
strfont=font.Font(size=25)
framefont=font.Font(size=16)

yourcard=[]
comcard=[]

grid_list=[(1,1),()]

def game():
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))

    #相手
    textcomcard=tk.StringVar()
    textcomcard.set("{}".format(comcard))
    textcomcard_sum=tk.StringVar()
    textcomcard_sum.set("相手の合計:{}".format(sum(comcard)))

    #自分
    textyourcard=tk.StringVar()
    textyourcard.set("{}".format(yourcard))
    textyourcard_sum=tk.StringVar()
    textyourcard_sum.set("あなたの合計:{}".format(sum(yourcard)))
