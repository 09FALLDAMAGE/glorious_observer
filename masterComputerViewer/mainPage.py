import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Canvas
from errorHandeler import *


class mainPage(tk.Tk):
    def __init__(self, Tn):
        super(mainPage, self).__init__()

        self.geo = [1535, 840]

        self.title(f"Master Viewer V{'1.0'}")

        self.graphPos = [60, 400]

        self.mode = [
            "Dark",
            "Light"
        ]

        self.geometry(f"{self.geo[0]}x{self.geo[1]}")
        self.canvas = Canvas(self, width=self.geo[0], height=self.geo[1])
        self.canvas.pack()

        self.data1 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Total Points': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
                      }

        self.data2 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Auto Points': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
                      }

        self.data3 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'TeleCubes': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
                      }

        self.data4 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'TeleCones': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
                      }

        self.data5 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Endgame': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
                      }

        self.options = [
            "Total Match Points",
            "Auto Points",
            "TeleCubes",
            "TeleCones",
            "Endgame Balance"
        ]

        global totals
        global auto
        global cubes
        global cones
        global endGame

        self.teamID = Tn

        self.variable = tk.StringVar()
        self.variable.set(self.options[0])
        self.thing(self.options[0])

        self.modeVar = tk.StringVar()
        self.modeVar.set(self.mode[0])
        self.modes(self.mode[0])

    def thing(self, event):
        df1 = pd.DataFrame(self.data1)

        df2 = pd.DataFrame(self.data2)

        df3 = pd.DataFrame(self.data3)

        df4 = pd.DataFrame(self.data4)

        df5 = pd.DataFrame(self.data5)

        if event == self.options[0]:
            try:
                self.kill()

                figure1 = plt.Figure(figsize=(5, 4), dpi=100)
                ax1 = figure1.add_subplot(111)
                totals = FigureCanvasTkAgg(figure1, self)
                totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
                df1.plot(kind='line', legend=True, ax=ax1, color='blue', marker='o', fontsize=10)
                ax1.set_title('Total Points')

                totals.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure1 = plt.Figure(figsize=(5, 4), dpi=100)
                ax1 = figure1.add_subplot(111)
                totals = FigureCanvasTkAgg(figure1, self)
                totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
                df1.plot(kind='line', legend=True, ax=ax1, color='red', marker='o', fontsize=10)
                ax1.set_title('Total Points')

                totals.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[1]:
            try:
                self.kill()

                figure2 = plt.Figure(figsize=(5, 4), dpi=100)
                ax2 = figure2.add_subplot(111)
                auto = FigureCanvasTkAgg(figure2, self)
                auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
                df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
                ax2.set_title('Auton Points Per Match')

                auto.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure2 = plt.Figure(figsize=(5, 4), dpi=100)
                ax2 = figure2.add_subplot(111)
                auto = FigureCanvasTkAgg(figure2, self)
                auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
                df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
                ax2.set_title('Auton Points Per Match')

                auto.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[2]:
            try:
                self.kill()

                figure3 = plt.Figure(figsize=(5, 4), dpi=100)
                ax3 = figure3.add_subplot(111)
                cubes = FigureCanvasTkAgg(figure3, self)
                cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
                df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
                ax3.set_title('Teleop Cubes per Match')

                cubes.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure3 = plt.Figure(figsize=(5, 4), dpi=100)
                ax3 = figure3.add_subplot(111)
                cubes = FigureCanvasTkAgg(figure3, self)
                cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
                df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
                ax3.set_title('Teleop Cubes per Match')

                cubes.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[3]:
            try:
                self.kill()

                figure4 = plt.Figure(figsize=(5, 4), dpi=100)
                ax4 = figure4.add_subplot(111)
                cones = FigureCanvasTkAgg(figure4, self)
                cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df4 = df4[['Match', 'TeleCubes']].groupby('Match').sum()
                df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
                ax4.set_title('Teleop Cones per Match')

                cones.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure4 = plt.Figure(figsize=(5, 4), dpi=100)
                ax4 = figure4.add_subplot(111)
                cones = FigureCanvasTkAgg(figure4, self)
                cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df4 = df4[['Match', 'TeleCones']].groupby('Match').sum()
                df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
                ax4.set_title('Teleop Cones per Match')

                cones.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[4]:
            try:
                self.kill()

                figure5 = plt.Figure(figsize=(5, 4), dpi=100)
                ax5 = figure5.add_subplot(111)
                endGame = FigureCanvasTkAgg(figure5, self)
                endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
                df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
                ax5.set_title('Endgame Points')

                endGame.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure5 = plt.Figure(figsize=(5, 4), dpi=100)
                ax5 = figure5.add_subplot(111)
                endGame = FigureCanvasTkAgg(figure5, self)
                endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
                df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
                ax5.set_title('Endgame Points')
                endGame.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

    def kill(self):
        totals.get_tk_widget().destroy()
        auto.get_tk_widget().destroy()
        cubes.get_tk_widget().destroy()
        cones.get_tk_widget().destroy()
        endGame.get_tk_widget().destroy()

    def teamImage(self):
        image = Image.open(f"{self.teamID}.jpg")

        # Resize the image using resize() method
        resize_image = image.resize((413, 310))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = tk.Label(image=img)
        label1.image = img
        label1.pack()

        label1.place(x=100, y=30)

    def teamTitles(self):
        self.canvas.create_text(self.geo[0] / 2, 40, text=f'Team {self.teamID}', font=('Arial', 25))
        self.canvas.create_text(self.geo[0] / 2, 90, text=f'The Monsters', font=('Arial', 25))

    def modes(self, event):
        if event == self.mode[0]:
            try:
                self.canvas.delete('backGround')

                self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], tags='backGround', fill='grey')
                self.canvas.lower('backGround')
            except:
                self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], tags='backGround', fill='grey')
                self.canvas.lower('backGround')

        elif event == self.mode[1]:
            try:
                self.canvas.delete('backGround')

                self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], tags='backGround', fill='white')
                self.canvas.lower('backGround')
            except:
                self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], tags='backGround', fill='white')
                self.canvas.lower('backGround')

    def pitDisplay(self):
        # finals
        self.canvas.create_text(700, 200, text='Drive Type', font=('Arial', 15))

        self.canvas.create_text(700, 275, text='Weight', font=('Arial', 15))

        self.canvas.create_text(700, 350, text='Size', font=('Arial', 15))

        self.canvas.create_text(700, 225, text='Tank', font=('Arial', 15))

        self.canvas.create_text(700, 300, text='110 lbs', font=('Arial', 15))

        self.canvas.create_text(700, 375, text='2ft, 25% of Charger', font=('Arial', 15))

    def makeDrops(self):
        drop = tk.OptionMenu(self, self.variable, *self.options, command=self.thing)
        drop.pack()
        drop.place(x=250, y=360, in_=self)

        modeDrop = tk.OptionMenu(self, self.modeVar, *self.mode, command=self.modes)
        modeDrop.pack()
        modeDrop.place(x=15, y=15, in_=self)

    def createHUD(self):
        self.teamImage()
        self.teamTitles()
        self.pitDisplay()
        self.makeDrops()
        self.mainloop()
