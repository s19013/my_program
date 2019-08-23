import tkinter
import tkinter as tk
import random
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import sys
from tkinter import messagebox
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
    def battle():
        if sum(yourcard)>sum(comcard):
            info.set("あなたの勝ち")
            con()
        elif sum(yourcard)<sum(comcard):
            info.set("あなたの負け")
            con()
    def con():
        q=messagebox.askyesno("コンテニュー","続けますか？")
        if q==True:
            game()
        else:
            win.destroy

    def comturn():
        if sum(comcard)<=15:
            while True:
                comcard.append(random.randint(1,13))
                textyourcard.set("{}".format(comcard))
                textcomcard_sum.set("{}".format(sum(comcard)))
                if sum(comcard)>21:
                    info.set("相手がバーストしました")
                    break
                else:
                    battle()
                    break
        else:
            battle()

    def update_yourcard():
        yourcard.append(random.randint(1,13))
        textyourcard.set("{}".format(yourcard))
        textyourcard_sum.set("あなたの合計:{}".format(sum(yourcard)))
        if sum(yourcard)>21:
            info.set("バーストしました (ﾉд-｡)ｸｽﾝ\nゲームオーバー")
            time.sleep(1)
            con()



    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    if sum(yourcard)>21:
        info.set("バーストしました (ﾉд-｡)ｸｽﾝ\nゲームオーバー")
        bhit.pack_forget()
        bstand.pack_forget()

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
    bhit=tk.Button(etcside,text="hit",command=update_yourcard)
    bhit.pack(side="left",padx=(225,50))
    bstand=tk.Button(etcside,text="stand",command=comturn)
    bstand.pack(side="left")
    #自分
    textyourcard=tk.StringVar()
    textyourcard.set("{}".format(yourcard))
    textyourcard_sum=tk.StringVar()
    textyourcard_sum.set("あなたの合計:{}".format(sum(yourcard)))

    lmycord=tk.Label(yourside,font=strfont,textvariable=textyourcard).pack(side="left")
    lmycord_sum=tk.Label(yourside,font=strfont,textvariable=textyourcard_sum).pack(side="right")



#---------------------------------------

#実行
game()
win.mainloop()
