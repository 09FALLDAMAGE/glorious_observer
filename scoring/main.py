import tkinter as tk


class fattass(tk.Tk):
    def __init__(self):
        super(fattass, self).__init__()

        self.geo = [1035, 800]

        self.inkConservationMode = False

        self.title("fatass")

        self.geometry(f"{self.geo[0]}x{self.geo[1]}")
        self.canvas = tk.Canvas(self, width=self.geo[0], height=self.geo[1])
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], fill='white')

        self.visiableBall = True

        self.Labelx = 200
        self.Labely = 500
        self.Labelendx = self.Labelx + 100
        self.Labelendy = self.Labely + 100

        self.box = self.canvas.create_rectangle(
            self.Labelx,
            self.Labely,
            self.Labelendx,
            self.Labelendy,
            fill="Red"
        )

        self.box1 = self.canvas.create_rectangle(
            self.Labelx,
            self.Labely,
            self.Labelendx,
            self.Labelendy,
            fill="Blue"
        )

        self.canvas.itemconfig(self.box, state="normal")
        self.canvas.tag_bind(self.box, "<Button-1>", self.cursorBalls)

        self.canvas.itemconfig(self.box1, state="hidden")
        self.canvas.tag_bind(self.box1, "<Button-1>", self.cursorBalls)

        self.canvas.pack()

    def cursorBalls(self, event):
        self.visiableBall = not self.visiableBall
        print('balls', event.x, event.y)
        if (self.visiableBall):
            # self.Label.lower(belowThis=self.canvas)
            self.canvas.itemconfig(self.box1, state='hidden')
            self.canvas.itemconfig(self.box, state="normal")
        else:
            self.canvas.itemconfig(self.box1, state="normal")
            self.canvas.itemconfig(self.box, state="hidden")
            # self.Label.lift(aboveThis=self.canvas)
        self.canvas.pack()


fattass().mainloop()
