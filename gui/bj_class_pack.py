import tkinter as tk
import random
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("My application")
        master.geometry("600x600")
        self.pack()
        #フォント
        self.strfont=font.Font(size=25)
        self.framefont=font.Font(size=16)

        #フレーム
        self.comside=tk.LabelFrame(master,bd=3,relief="groove",text="相手",font=self.framefont)
        self.comside.pack(fill="x")

        self.etcside=tk.Frame(master)
        self.etcside.pack(fill="x")

        self.myside=tk.LabelFrame(master,bd=3,relief="groove",text="あなた",font=self.framefont)
        self.myside.pack(fill="x")

        self.game()



    def one_more(self):
        dele1=self.comside.winfo_children()
        dele2=self.etcside.winfo_children()
        dele3=self.myside.winfo_children()
        for child in dele1:
            child.destroy()
        for child in dele2:
            child.destroy()
        for child in dele3:
            child.destroy()
        self.game()




    def battle(self):
        if sum(self.mycard)>sum(self.comcard):
            self.linfo["text"]="あなたの勝ち"
            self.con()
        elif sum(self.mycard)<sum(self.comcard):
            self.linfo["text"]="あなたの負け"
            self.con()
        else:
            self.linfo["text"]="引き分け"
            self.con()

    def con(self):
        self.bhit.destroy()
        self.bstand.destroy()
        self.linfo2["text"]="続けますか"
        self.cont=tk.Button(self.etcside,text="continue",command=self.one_more)
        self.cont.pack(side="left",padx=(210,50))
        self.exit=tk.Button(self.etcside,text="exit",command=lambda:root.destroy())
        self.exit.pack(side="left")

    def comturn(self):
        while sum(self.comcard)<=20:
            self.comcard.append(random.randint(1,13))
            self.lcomcard["text"]="{}".format(self.comcard)
            self.lcomcard_sum["text"]="相手の合計:{}".format(sum(self.comcard))
        if sum(self.comcard)>21:
            self.linfo['text']="相手がバーストしました"
            self.con()
        else:
            self.battle()

    def update_mycard(self):
        self.mycard.append(random.randint(1,13))
        self.lmycard["text"]="{}".format(self.mycard)
        self.lmycard_sum["text"]="あなたの合計:{}".format(sum(self.mycard))
        if sum(self.mycard)>21:
            self.linfo["text"]="バーストしました"
            #time.sleep(1)
            self.con()

    def game(self):

        #関数in関数
        #ここはオブジェクト指向だと少し楽かも同じ作業だし
        self.mycard=[]
        self.comcard=[]


        for i in range(2):
            self.mycard.append(random.randint(1,13))
            self.comcard.append(random.randint(1,13))

        #相手
        # self.textcomcard=tk.StringVar()
        # self.textcomcard.set("{}".format(self.comcard))
        # self.textcomcard_sum=tk.StringVar()
        # self.textcomcard_sum.set("相手の合計:{}".format(sum(self.comcard)))

        self.lcomcard=tk.Label(self.comside,font=self.strfont,text="{}".format(self.comcard),anchor=tk.W)
        self.lcomcard.pack(side="left")
        self.lcomcard_sum=tk.Label(self.comside,font=self.strfont,text="相手の合計:{}".format(sum(self.comcard)),anchor=tk.E)
        self.lcomcard_sum.pack(side="right")
        #中央
        # self.info=tk.StringVar()
        # self.info.set("hit or stand")
        self.linfo=tk.Label(self.etcside,text="hit or stand",font=self.framefont,anchor=tk.N)
        self.linfo.pack()
        # self.info2=tk.StringVar()
        # self.info2.set("")
        self.linfo2=tk.Label(self.etcside,text="",font=self.framefont,anchor=tk.N)
        self.linfo2.pack()
        self.bhit=tk.Button(self.etcside,text="hit",command=self.update_mycard)
        self.bhit.pack(side="left",padx=(225,50))
        self.bstand=tk.Button(self.etcside,text="stand",command=self.comturn)
        self.bstand.pack(side="left")
        #自分
        # self.textmycard=tk.StringVar()
        # self.textmycard.set("{}".format(self.mycard))
        # self.textmycard_sum=tk.StringVar()
        # self.textmycard_sum.set("あなたの合計:{}".format(sum(self.mycard)))

        self.lmycard=tk.Label(self.myside,font=self.strfont,text="{}".format(self.mycard))
        self.lmycard.pack(side="left")
        self.lmycard_sum=tk.Label(self.myside,font=self.strfont,text="あなたの合計:{}".format(sum(self.mycard)))
        self.lmycard_sum.pack(side="right")

        if sum(self.mycard)>21:
            self.linfo["text"]="バーストしました"
            self.con()

        if sum(self.comcard)>21:
            self.linfo['text']="相手がバーストしました"
            self.con()
#class Destroy:
#    def __init__(self):




root = tk.Tk()
app = Application(master=root)
app.mainloop()
