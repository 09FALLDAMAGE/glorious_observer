# Import the required libraries
from tkinter import *
from tkinter import ttk

root = Tk()

geo = [1535, 840]

graphPos = [60, 400]

mode = [
    "Dark",
    "Light"
]

root.geometry(f"{geo[0]}x{geo[1]}")
canvas = Canvas(root, width=geo[0], height=geo[1])
canvas.pack()


frame = Frame(root, bg="skyblue3", width=700, height=250)
frame.pack()
frame.place(x=500, y=10)

root.mainloop()
