from tkinter import *
from tkinter import ttk

def button1_clicked():
    print('man = %s' % man.get())
    quit()

def cb_selected(event):
    print('man = %s' % man.get())

if __name__ == '__main__':
    root = Tk()
    root.title('Combobox 1')

    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # Combobox
    man = StringVar()
    cb = ttk.Combobox(frame1, textvariable=man)
    cb.bind('<<ComboboxSelected>>', cb_selected)

    cb['values']=('Foo', 'Bar', 'Baz')
    cb.set("Foo")
    cb.grid(row=0, column=0)

    #Button
    button1 = ttk.Button(frame1, text='OK', command=button1_clicked)
    button1.grid(row=0, column=1)

    root.mainloop()
