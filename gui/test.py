import tkinter as tk

win=tk.Tk()
win.geometry("500x500")

for i in range(25):
    a=tk.Label(win,text="-"*500)
    a.place(x=0,y=i*50)
    b=tk.Label(win,text="|\n"*500)
    b.place(x=i*50,y=0)

win.mainloop()
