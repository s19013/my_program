import tkinter as tk
root = tk.Tk().title("Visualizer for function")
# ボタンが押されたときのコールバック関数
#def btn0_callback():
#    print("ボタン0が押されました")
#def btn1_callback():
#    print("ボタン1が押されました")
#def btn2_callback():
#    print("ボタン2が押されました")#

## ボタンの作成
#button0 = tk.Button(root,text="0",command=btn0_callback)
#button0.pack(fill="x")
#button1 = tk.Button(root,text="1",command=btn1_callback)
#button1.pack(fill="x")
#button2 = tk.Button(root,text="2",command=btn2_callback)
#button2.pack(fill="x")

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)

    def make_bottun(self,i):
        self.i=i
        buttun=tk.Button(root,text=self.i,command=lambda: print("ボタン{}が押されました".format(self.i)))
        buttun.pack(fill="x")


a=Application()
for i in range(3):
    a.make_bottun(i)

app = Application(master = root)
app.mainloop()
