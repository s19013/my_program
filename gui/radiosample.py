import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Check Button Example")
        self.geometry("+{}+{}".format(300, 300))
        self.set_widgets()

    def set_widgets(self):
        self.frame = tk.Frame(self, bg="white",
                              width=300, height=300)
        self.frame.pack()
        self.button_radio = tk.Button(self.frame, text="sample",
                                      relief="groove", command=self.get_radio)
        self.button_radio.place(x=200, y=150)
        self.button_quit = tk.Button(self.frame, text="quit",
                                     relief="groove", command=self.quit)
        self.button_quit.place(x=200, y=200)
        ### Ratio Button ###
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.radio_o = tk.Radiobutton(self.frame, text="o", value=1,
                                      variable=self.radio_var)
        self.radio_x = tk.Radiobutton(self.frame, text="x", value=0,
                                      variable=self.radio_var)
        self.radio_o.place(x=100, y=100)
        self.radio_x.place(x=100, y=120)

    def get_radio(self):
        print(self.radio_var.get())

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
