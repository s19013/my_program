import tkinter as tk


hoge = [
    ["(", ")", "%", "**", "ac"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "/"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


# ボタンの定義
def make_click(button):
    def click(s):
        if button == '=':
            calc(0)
        elif button == 'ac':
            display.delete(0, tk.END)
            label["text"] = ''
        else:
            display.insert(tk.END, button)
    return click


# 式を計算
def calc(s):
    try:
        label["text"] = '= ' + str(eval(display.get()))
    except SyntaxError:
        label["text"] = "その式では計算できません"
    except NameError:
        label["text"] = "数字を入力してください"
    except TypeError:
        label["text"] = "数字を入力してください"


# ウィンドウを作成
win = tk.Tk()
win.title('電卓')
win.geometry("700x700")


# ディスプレイを作成
display = tk.Entry(win, font=('', 20), justify="center")
display.pack(fill='x')
display.bind('<1>', calc)
label = tk.Label(win, font=('', 20), justify="center")
label.pack(fill='x')


# ボタンの一括作成
frame = tk.Frame(win)
frame.pack()
for Y, cols in enumerate(hoge):
    for X, num in enumerate(cols):
        BTN = tk.Button(frame, text=num, font=('', 25), width=4, height=2)
        BTN.grid(row=Y, column=X)
        BTN.bind('<1>', make_click(num))


# ウィンドウをループ
win.mainloop()
