import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import font
from time import sleep
from email.mime.text import MIMEText
import smtplib
#ウィンドウ
win=tk.Tk()
win.geometry("500x500")

#関数
def ok():
    def ok_click():
        info.grid_remove()
        okbutton.grid_remove()
        backbutton.grid_remove()
        info2=tk.Label(sub_win,font=info_font,text="登録しました")
        info2.pack()
        quitbutton=tk.Button(sub_win,text="quit",command=lambda: sub_win.quit())
        quitbutton.pack()
        # SMTP認証情報
        account = "s19013@std.it-college.ac.jp"
        password = "gemini0522"

        # 送受信先
        to_email = "hideya670@gmail.com"
        from_email = "s19013@std.it-college.ac.jp"

        # MIMEの作成
        subject = "テストメール"
        message = """名字:{}  名前:{}\n
        血液型:{}\n
        性別:{}\n
        生年月日:{}年{}月{}日\n
        メールアドレス:{}\n
        パスワード:{}\n
        """.format(myouzi.get(),namae.get(),blat,sex,year.get(),manth.get(),day.get(),email.get(),password.get())
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email

        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

    info_font=font.Font(size=15)
    sub_win=Toplevel()
    sub_win.geometry("500x500")
    blat_list=["a","b","ab","o"]
    sex_list=["男","女"]
    blat=blat_list[radio_blat.get()]
    sex=sex_list[radio_sex.get()]
    info=tk.Label(sub_win,justify="left",font=info_font,
    text="""   ご確認ください\n
    名字:{}  名前:{}\n
    血液型:{}\n
    性別:{}\n
    生年月日:{}年{}月{}日\n
    メールアドレス:{}\n
    パスワード:{}\n
    よろしければ[ok]ボタンを押してください"""
    .format(myouzi.get(),namae.get(),blat,sex,year.get(),manth.get(),day.get(),email.get(),password.get()))
    info.grid(row=0,column=0,columnspan=4)
    okbutton=tk.Button(sub_win,text="ok",command=ok_click)
    okbutton.grid(row=1,column=0,padx=120)
    backbutton=tk.Button(sub_win,text="back",command=lambda: sub_win.destroy())
    backbutton.grid(row=1,column=1,padx=10)

#部品
#名前入力
Lmyouzi=tk.Label(win,text="名字")
myouzi=tk.Entry()
Lnamae=tk.Label(win,text="名前")
namae=tk.Entry()
#ラジオボタン
#blat
radio_blat=tk.IntVar()
radio_blat.set(0)
Lblat=tk.Label(win,text="あなたの血液型は")
radio_blat_a=tk.Radiobutton(win,text="a", value=0,variable=radio_blat)
radio_blat_b=tk.Radiobutton(win,text="b", value=1,variable=radio_blat)
radio_blat_ab=tk.Radiobutton(win,text="ab", value=2,variable=radio_blat)
radio_blat_o=tk.Radiobutton(win,text="o", value=3,variable=radio_blat)
#sex
radio_sex=tk.IntVar()
radio_sex.set(0)
Lsex=tk.Label(win,text="性別は")
radio_sex_male=tk.Radiobutton(win,text="男",value=0,variable=radio_sex)
radio_sex_female=tk.Radiobutton(win,text="女",value=1,variable=radio_sex)
#ボタン
button_ok=tk.Button(win,text="ok",command=ok)
#ドロップダウン
Ldrop=tk.Label(win,text="生年月日を選んでください[年/月/日]")
#year
year=StringVar()
year_cb=ttk.Combobox(win,textvariable=year,width=10)
year_cb["values"]=(list(range(1900, 2020)))
year_cb.set("2019")
#manth
manth=StringVar()
manth_cb=ttk.Combobox(win,textvariable=manth,width=10)
manth_cb["values"]=(list(range(1, 13)))
manth_cb.set("1")
#day
day=StringVar()
day_cb=ttk.Combobox(win,textvariable=day,width=10)
day_cb["values"]=(list(range(1, 32)))
day_cb.set("1")
#addres
Lemail=tk.Label(win,text="emailアドレス").grid(row=9,column=0,sticky=tk.W)
email=tk.Entry()
Lpassword=tk.Label(win,text="パスワード").grid(row=10,column=0,sticky=tk.W)
password=tk.Entry()

#表示
#名前
Lmyouzi.grid(row=0,column=0,columnspan=4,sticky=tk.W)
Lnamae.grid(row=0,column=2,columnspan=4,sticky=tk.W)
myouzi.grid(row=1,column=0,columnspan=4,sticky=tk.W)
namae.grid(row=1,column=2,columnspan=4,sticky=tk.W)
#blat
Lblat.grid(row=2, column=0,sticky=tk.W)
radio_blat_a.grid(row=3, column=0)
radio_blat_b.grid(row=3, column=1)
radio_blat_ab.grid(row=3, column=2)
radio_blat_o.grid(row=3, column=3)
#性別
Lsex.grid(row=4,column=0,sticky=tk.W)
radio_sex_male.grid(row=5,column=0)
radio_sex_female.grid(row=5,column=1)
#ドロップ
Ldrop.grid(row=6,column=0,sticky=tk.W,pady=10,columnspan=4)
year_cb.grid(row=8,column=0,sticky=tk.N+tk.E+tk.S)
manth_cb.grid(row=8,column=1)
day_cb.grid(row=8,column=2)
#addres
email.grid(row=9,column=1,columnspan=4,pady=10,sticky=tk.W)
password.grid(row=10,column=1,sticky=tk.W)
#ボタン
button_ok.place(x=220,y=300)
win.mainloop()


#サブスクリーン
