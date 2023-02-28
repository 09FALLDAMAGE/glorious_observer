import tkinter as tk
import random


class william(tk.Tk):
    def __init__(self):
        super(william, self).__init__()
        w = 100
        h = 100
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = random.randint(0, ws - w)
        y = random.randint(0, hs - h)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window = tk.Canvas(self, width=0, height=0)
        self.window.pack()

    def kill(self):
        self.destroy()

    def creategui(self):
        button = tk.Button(self, width=300, height=999, command=self.kill)
        button.place(x=0, y=0)
        self.mainloop()


while True:
    william().creategui()
