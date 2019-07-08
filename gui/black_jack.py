import Tkinter as tk
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import font

win=tk.Tk()
win.geometry("600x600")

#フレーム
comside=ttk.Frame(win,width=600,height=250)
etcside=ttk.Frame(win,width=600,height=100)
my_side=ttk.Frame(win,width=600,height=250)
#部品
mylabel=tk.Label(my_side,text=mynumber).grid(row=0,column=0)
comlabel=tk.Label(comside,text=comnumber).grid(row=0,column=0)
#-----------------------------
def game():
