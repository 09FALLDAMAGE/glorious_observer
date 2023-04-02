import tkinter as tk
from constants import *
from tkinter import Canvas
from requestHandeler import requests
from dataTables import dataTables


class interface(tk.Tk):
    def __init__(self):
        super(interface, self).__init__()

        self.geometry("250x140")

        self.title(f'Sheet UI V{constants.version}')

        self.match_var = tk.StringVar()
        self.json_var = tk.StringVar()

        self.eventCode = tk.StringVar()

        self.canvas = Canvas(self, width=250, height=140)
        self.canvas.pack()

        # self.canvas.create_rectangle(10, 110, 240, 130, fill='red')

    def loadingBar(self, barState):
        old = True
        # self.canvas.create_rectangle(10, 110, 10 + (barState * 5), 130, fill='light green')

    def getMatches(self):
        requests.refresh(self.eventCode.get())

    def submit(self):
        matchReq = self.match_var.get()
        JsonReq = self.json_var.get()

        requests().start(matchReq, JsonReq)

        self.match_var.set("")

    def createGUI(self):
        match_label = tk.Label(self, text='Match', font=('calibre', 10, 'bold'))

        match_entry = tk.Entry(self, textvariable=self.match_var, font=('calibre', 10, 'normal'))

        json_label = tk.Label(self, text='Json Path', font=('calibre', 10, 'bold'))

        json_entry = tk.Entry(self, textvariable=self.json_var, font=('calibre', 10, 'normal'))

        sub_btn = tk.Button(self, text='generate', command=self.submit)

        ref_entry = tk.Entry(self, textvariable=self.eventCode, font=('calibre', 10, 'normal'))

        ref_btn = tk.Button(self, text='refresh', command=self.getMatches)

        json_entry.insert(0, constants.jsonName)

        match_label.place(x=23, y=10)
        match_entry.place(x=80, y=10)

        json_label.place(x=10, y=40)
        json_entry.place(x=80, y=40)

        sub_btn.place(x=100, y=70)

        ref_entry.place(x=90, y=110)
        ref_btn.place(x=15, y=105)

        self.loadingBar(0)

        # match_label.grid(row=0, column=0)
        # match_entry.grid(row=0, column=1)
        # json_label.grid(row=1, column=0)
        # json_entry.grid(row=1, column=1)
        # sub_btn.grid(row=2, column=1)

        self.mainloop()
