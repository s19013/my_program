import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        # Window
        self.title("三目並べ")
        self.geometry("{}x{}+{}+{}".format(360, 400, 450, 100))

    def run(self):
        self.mainloop()

    def set_variables(self):
        self.result = 0
        self.playerTurn = 1
        self.board2info = [0] * 9
        self.symbol = " ox"
        self.alpstr = "abcdefghi"
        self.winner = ["", "あなた", "引き分け", "CPU"]


if __name__ == "__main__":
    app = App()
    app.run()
