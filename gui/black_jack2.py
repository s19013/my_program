import tkinter
import tkinter as tk
import random
import sys
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
#フレーム
comside=tk.LabelFrame(win,bd=3,relief="groove",text="相手",font=framefont)
comside.pack(fill="x")

etcside=tk.Frame(win)
etcside.pack(fill="x")

yourside=tk.LabelFrame(win,bd=3,relief="groove",text="あなた",font=framefont)
yourside.pack(fill="x")

yourcard=[]
comcard=[]
#部品
#-----------------------------
#関数
def game():
    #関数in関数
    #ここはオブジェクト指向だと少し楽かも同じ作業だし

    def comturn():
        while sum(comcard)<=15:
            append.comcard(random.randint(1,13))
            textmycard.set("{}".format(comcard))
            textcomcard_sum.set("{}".format(sum(comcard)))
            if sum(comcard)>21:
                barst_com()

    def barst_com():
        info.set("相手がバーストしました")
        bhit.pack_forget()
        bstand.pack_forget()
        return True



    def update_mycard():
        yourcard.append(random.randint(1,13))
        textmycard.set("{}".format(yourcard))
        textmycard_sum.set("あなたの合計:{}".format(sum(yourcard)))
        if sum(yourcard)>21:
            info.set("バーストしました (ﾉд-｡)ｸｽﾝ\nゲームオーバー")
            bhit.pack_forget()
            bstand.pack_forget()
            return False

    def end():
        if barst_com==False or update_mycard==False:
            time.sleep(1)
            sys.exit


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
    bhit=tk.Button(etcside,text="hit",command=update_mycard)
    bhit.pack(side="left",padx=(225,50))
    bstand=tk.Button(etcside,text="stand",command=lambda :comturn())
    bstand.pack(side="left")
    #自分
    textmycard=tk.StringVar()
    textmycard.set("{}".format(yourcard))
    textmycard_sum=tk.StringVar()
    textmycard_sum.set("あなたの合計:{}".format(sum(yourcard)))

    lmycord=tk.Label(yourside,font=strfont,textvariable=textmycard).pack(side="left")
    lmycord_sum=tk.Label(yourside,font=strfont,textvariable=textmycard_sum).pack(side="right")

#---------------------------------------

#実行
game()
win.mainloop()
