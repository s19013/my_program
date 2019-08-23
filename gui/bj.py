import tkinter
import tkinter as tk
import random
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time

win=tk.Tk()
win.geometry("900x900")
#フォント
strfont=font.Font(size=25)
framefont=font.Font(size=16)

yourcard=[]
comcard=[]

#lene,enecard,lenesum,enesum
#
#lyou,yourcard,lyousum,yousum

def game():
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))

    #相手
    textcomcard=tk.StringVar()
    textcomcard.set("{}".format(comcard))
    textcomcard_sum=tk.StringVar()
    textcomcard_sum.set("相手の合計:{}".format(sum(comcard)))

    lcomcard=tk.Label(win,font=strfont,textvariable=textcomcard)
    lcomcard_sum=tk.Label(win,font=strfont,textvariable=textcomcard_sum)
    lcomcard_sum.grid(row=0,column=0,sticky=tk.S)

    #中央
    # info=tk.StringVar()
    # info.set("hit or stand")
    # linfo=tk.Label(win,textvariable=info,font=framefont)
    # bhit=tk.Button(win,text="hit",command=update_yourcard)
    # bstand=tk.Button(win,text="stand",command=lambda :comturn())


    #自分
    textyourcard=tk.StringVar()
    textyourcard.set("{}".format(yourcard))
    textyourcard_sum=tk.StringVar()
    textyourcard_sum.set("あなたの合計:{}".format(sum(yourcard)))

    lyourcord=tk.Label(win,font=strfont,textvariable=textyourcard)
    lyourcord_sum=tk.Label(win,font=strfont,textvariable=textyourcard_sum)

    #grid_list=[(lcomcard,0,0,tk.W),(lcomcard_sum,0,2,tk.E)]
    #for name,x,y,a in grid_list:
        #name.grid(row=x,column=y,sticky=a)




game()
win.mainloop()
