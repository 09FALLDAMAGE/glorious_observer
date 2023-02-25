import tkinter as tk
from requestHandeler import *
from constants import *


class interface(tk.Tk):
    def __init__(self):
        super(interface, self).__init__()

        self.geometry("250x100")

        self.title(f'Sheet UI V{constants.version}')

        self.match_var = tk.StringVar()
        self.json_var = tk.StringVar()

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

        json_entry.insert(0, constants.jsonName)

        match_label.grid(row=0, column=0)
        match_entry.grid(row=0, column=1)
        json_label.grid(row=1, column=0)
        json_entry.grid(row=1, column=1)
        sub_btn.grid(row=2, column=1)

        self.mainloop()