import tkinter as tk

# ボタンを押したときの処理 --- (*1)
def calc_bmi():
    # BMIを計算
    h = float(textHeight.get()) / 100
    w = float(textWeight.get())
    bmi = w / h ** 2
    rw = h ** 2 * 22
    per = int(w / rw * 100) - 100
    # 結果をラベルに表示
    s = "肥満 {0}% (bmi={1})".format(per, bmi)
    labelResult['text'] = s

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("肥満判定")
win.geometry("500x250")

# 部品を作成 --- (*3)
labelHeight = tk.Label(win, text='身長(cm):')
labelHeight.pack()

textHeight = tk.Entry(win)
textHeight.pack()

labelWeight = tk.Label(win, text='体重(kg):')
labelWeight.pack()

textWeight = tk.Entry(win)
textWeight.pack()

labelResult = tk.Label(win, text='---')
labelResult.pack()

calcButton = tk.Button(win, text='計算')
calcButton["command"] = calc_bmi
calcButton.pack()

# ウィンドウを動かす
win.mainloop()
