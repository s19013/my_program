import tkinter as tk
import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk

win=tk.Tk()
win.geometry("600x600")
#フォント
strfont=font.Font(size=25)
framefont=font.Font(size=16)
#フレーム
comside=tk.LabelFrame(win,bd=3,relief="groove",text="相手",font=framefont)
comside.pack(fill="x")

etcside=tk.Frame(win)
etcside.pack(fill="x")

yourside=tk.LabelFrame(win,bd=3,relief="groove",text="あなた",font=framefont)
yourside.pack(fill="x")
#部品
#-----------------------------
#関数
def game():
    #関数in関数
    #ここはオブジェクト指向だと少し楽かも同じ作業だし
    def update_mycard():
        yourcard.append(random.randint(1,13))
        textmycard.set("{}".format(yourcard))
        textmycard_sum.set("あなたの合計:{}".format(sum(yourcard)))
        return sum(yourcard)

    yourcard=[]
    comcard=[]
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    #相手
    textcomcard=tk.StringVar()
    textcomcard.set("{}".format(comcard))
    textcomcard_sum=tk.StringVar()
    textcomcard_sum.set("相手の合計:{}".format(sum(comcard)))

    lcomcard=tk.Label(comside,font=strfont,textvariable=textcomcard).pack(side="left",padx=(0,15))
    lcomcard_sum=tk.Label(comside,font=strfont,textvariable=textcomcard_sum).pack(side="right")
    #中央
    info=tk.StringVar()
    info.set("hit or stand")
    linfo=tk.Label(etcside,textvariable=info,font=framefont).pack()
    bhit=tk.Button(etcside,text="hit",command=update_mycard).pack(side="left",padx=(225,50))
    bstand=tk.Button(etcside,text="stand").pack(side="left")
    #自分
    textmycard=tk.StringVar()
    textmycard.set("{}".format(yourcard))
    textmycard_sum=tk.StringVar()
    textmycard_sum.set("あなたの合計:{}".format(sum(yourcard)))

    lmycord=tk.Label(yourside,font=strfont,textvariable=textmycard).pack(side="left")
    lmycord_sum=tk.Label(yourside,font=strfont,textvariable=textmycard_sum).pack(side="right")

#---------------------------------------
    if update_mycard()>21:
        info.set("バーストしました (ﾉд-｡)ｸｽﾝ\nゲームオーバー")

#実行
game()
win.mainloop()
