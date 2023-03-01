import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Canvas
from constants import *
from errorHandeler import *
from pitJson import getPitData
from jsonInterpreter import makeList, checkTeam

class mainPage(tk.Tk):
    def __init__(self):
        super(mainPage, self).__init__()

        self.label1 = None
        self.endGame = None
        self.cones = None
        self.auto = None
        self.cubes = None
        self.totals = None

        self.geo = [1535, 840]

        self.title(f"Master Viewer V{constants.vers}")

        self.graphPos = [60, 400]

        self.mode = [
            "Dark",
            "Light"
        ]

        self.geometry(f"{self.geo[0]}x{self.geo[1]}")
        self.canvas = Canvas(self, width=self.geo[0], height=self.geo[1])
        self.canvas.pack()

        self.data1 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Total Points': [15, 13, 12, 23, 17, 32, 10, 8, 6, 0]
                      }

        self.data2 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Auto Points': [5, 5, 5, 3, 0, 0, 0, 3, 2, 1]
                      }

        self.data3 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'TeleCubes': [3, 3, 2, 3, 0, 0, 1, 2, 3, 0]
                      }

        self.data4 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'TeleCones': [4, 5, 4, 3, 1, 2, 3, 1, 0, 0]
                      }

        self.data5 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'Endgame': [3, 2, 1, 2, 3, 1, 2, 1, 2, 0]
                      }


        self.options = [
            "Total Match Points",
            "Auto Points",
            "TeleCubes",
            "TeleCones",
            "Endgame Balance"
        ]

        self.teamID = tk.StringVar()
        self.teamNum = constants.defaultTeam

        self.variable = tk.StringVar()
        self.variable.set(self.options[0])
        self.thing(self.options[0])

        self.modeVar = tk.StringVar()
        self.modeVar.set(self.mode[0])
        self.modes(self.mode[0])

        self.canvas.create_rectangle(100, 30, 513, 340)
        self.canvas.create_text(306, 170, text='No Image Available', font=('Arial', 15))

        newDat = self.propData(self.teamNum)

        self.data1['Match'] = newDat['matchAxis']
        self.data1['Total Points'] = newDat['matchAxis']

        self.data2['Match'] = newDat['matchAxis']
        self.data2['Auto Points'] = newDat['Auton Total']

        self.data3['Match'] = newDat['matchAxis']
        self.data3['TeleCubes'] = newDat['TeleCubes']

        self.data4['Match'] = newDat['matchAxis']
        self.data4['TeleCones'] = newDat['TeleCones']

        self.data5['Match'] = newDat['matchAxis']
        self.data5['Endgame'] = newDat['eTotal']

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
                self.totals = FigureCanvasTkAgg(figure1, self)
                self.totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
                df1.plot(kind='line', legend=True, ax=ax1, color='blue', marker='o', fontsize=10)
                ax1.set_title('Total Points')

                self.totals.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure1 = plt.Figure(figsize=(5, 4), dpi=100)
                ax1 = figure1.add_subplot(111)
                self.totals = FigureCanvasTkAgg(figure1, self)
                self.totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
                df1.plot(kind='line', legend=True, ax=ax1, color='red', marker='o', fontsize=10)
                ax1.set_title('Total Points')

                self.totals.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[1]:
            try:
                self.kill()

                figure2 = plt.Figure(figsize=(5, 4), dpi=100)
                ax2 = figure2.add_subplot(111)
                self.auto = FigureCanvasTkAgg(figure2, self)
                self.auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
                df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
                ax2.set_title('Auton Points Per Match')

                self.auto.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure2 = plt.Figure(figsize=(5, 4), dpi=100)
                ax2 = figure2.add_subplot(111)
                self.auto = FigureCanvasTkAgg(figure2, self)
                self.auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
                df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
                ax2.set_title('Auton Points Per Match')

                self.auto.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[2]:
            try:
                self.kill()

                figure3 = plt.Figure(figsize=(5, 4), dpi=100)
                ax3 = figure3.add_subplot(111)
                self.cubes = FigureCanvasTkAgg(figure3, self)
                self.cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
                df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
                ax3.set_title('Teleop Cubes per Match')

                self.cubes.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure3 = plt.Figure(figsize=(5, 4), dpi=100)
                ax3 = figure3.add_subplot(111)
                self.cubes = FigureCanvasTkAgg(figure3, self)
                self.cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
                df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
                ax3.set_title('Teleop Cubes per Match')

                self.cubes.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[3]:
            try:
                self.kill()

                figure4 = plt.Figure(figsize=(5, 4), dpi=100)
                ax4 = figure4.add_subplot(111)
                self.cones = FigureCanvasTkAgg(figure4, self)
                self.cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df4 = df4[['Match', 'TeleCubes']].groupby('Match').sum()
                df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
                ax4.set_title('Teleop Cones per Match')

                self.cones.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure4 = plt.Figure(figsize=(5, 4), dpi=100)
                ax4 = figure4.add_subplot(111)
                self.cones = FigureCanvasTkAgg(figure4, self)
                self.cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df4 = df4[['Match', 'TeleCones']].groupby('Match').sum()
                df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
                ax4.set_title('Teleop Cones per Match')

                self.cones.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

        elif event == self.options[4]:
            try:
                self.kill()

                figure5 = plt.Figure(figsize=(5, 4), dpi=100)
                ax5 = figure5.add_subplot(111)
                self.endGame = FigureCanvasTkAgg(figure5, self)
                self.endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
                df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
                ax5.set_title('Endgame Points')

                self.endGame.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)
            except:
                figure5 = plt.Figure(figsize=(5, 4), dpi=100)
                ax5 = figure5.add_subplot(111)
                self.endGame = FigureCanvasTkAgg(figure5, self)
                self.endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
                df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
                ax5.set_title('Endgame Points')
                self.endGame.get_tk_widget().place(x=self.graphPos[0], y=self.graphPos[1], in_=self)

    def propData(self, teamNumber):
        teamDat = makeList(teamNumber)
        matchAxis = []
        matchesElapesed = len(makeList(self.teamNum)['Autonomous Cross Line'])
        for i in range(matchesElapesed):
            matchAxis.append(i + 1)

        fullData = {'matchAxis': matchAxis, 'Auton Total': teamDat['Autonomous Total'], 'TeleCones': teamDat['Teleop Total Cubes'], 'TeleCubes': teamDat['Teleop Total Cones'], 'eTotal': teamDat['Endgame Total']}

        return fullData

    def teamImage(self):

        try:
            image = Image.open(f"{self.teamNum}.jpg")

            # Resize the image using resize() method
            resize_image = image.resize((413, 310))

            img = ImageTk.PhotoImage(resize_image)

            # create label and add resize image
            self.label1 = tk.Label(image=img)
            self.label1.image = img
            self.label1.tag = 'updateContent'
            self.label1.pack()

            self.label1.place(x=100, y=30)
        except:
            filler3 = '17'

    def teamTitles(self):
        self.canvas.create_text(self.geo[0] / 2, 40, text=f'Team {self.teamNum}', font=('Arial', 25),
                                tags='updateContent')
        self.canvas.create_text(self.geo[0] / 2, 90, text=f'{getPitData(str(self.teamNum))["Name"]}', font=('Arial', 25), tags='updateContent')

    def pitDisplay(self):
        data = getPitData(str(self.teamNum))
        # finals
        self.canvas.create_text(700, 200, text='Drive Type', font=('Arial', 15), tags='updateContent')

        self.canvas.create_text(700, 275, text='Weight', font=('Arial', 15), tags='updateContent')

        self.canvas.create_text(700, 350, text='Size', font=('Arial', 15), tags='updateContent')

        self.canvas.create_text(700, 225, text=f'{data["Drivetrain"]}', font=('Arial', 15), tags='updateContent')

        self.canvas.create_text(700, 300, text=f'{data["Weight"]} Lbs', font=('Arial', 15), tags='updateContent')

        self.canvas.create_text(700, 375, text=f'{round(data["Width"]/ 12, constants.sigFigs)} x {round(data["Length"]/ 12, constants.sigFigs)} ft, {round((min([data["Width"]/ 12, data["Length"]/ 12]) / 8) * 100)}% of Charger', font=('Arial', 15), tags='updateContent')

    def kill(self):
        try:
            self.totals.get_tk_widget().destroy()
        except:
            filler = '21Savage'
        try:
            self.auto.get_tk_widget().destroy()
        except:
            filler = '21Savage'
        try:
            self.cubes.get_tk_widget().destroy()
        except:
            filler = '21Savage'
        try:
            self.cones.get_tk_widget().destroy()
        except:
            filler = '21Savage'
        try:
            self.endGame.get_tk_widget().destroy()
        except:
            filler = '21Savage'

    def update(self):
        self.teamNum = self.teamID.get()
        if checkTeam(self.teamNum):
            newDat = self.propData(self.teamNum)
            self.kill()
            try:
                self.canvas.delete('updateContent')
            except:
                filler2 = '21, can you do some for me'
            try:
                self.label1.destroy()
            except:
                filler2 = "hey sisters"

            self.data1['Match'] = newDat['matchAxis']
            self.data1['Total Points'] = newDat['matchAxis']

            self.data2['Match'] = newDat['matchAxis']
            self.data2['Auto Points'] = newDat['Auton Total']

            self.data3['Match'] = newDat['matchAxis']
            self.data3['TeleCubes'] = newDat['TeleCubes']

            self.data4['Match'] = newDat['matchAxis']
            self.data4['TeleCones'] = newDat['TeleCones']

            self.data5['Match'] = newDat['matchAxis']
            self.data5['Endgame'] = newDat['eTotal']

            self.teamTitles()
            self.pitDisplay()
            self.teamImage()
            self.thing(self.options[0])
        else:
            print('Not a Valid Team')

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

    def makeDrops(self):
        drop = tk.OptionMenu(self, self.variable, *self.options, command=self.thing)
        drop.pack()
        drop.place(x=250, y=360, in_=self)

        modeDrop = tk.OptionMenu(self, self.modeVar, *self.mode, command=self.modes)
        modeDrop.pack()
        modeDrop.place(x=15, y=15, in_=self)

    def makeEntry(self):
        teamSelect = tk.Entry(self, textvariable=self.teamID, font=('Arial', 12))

        sub_btn = tk.Button(self, text='Submit', command=self.update)

        teamSelect.place(x=950, y=30)
        sub_btn.place(x=1017, y=60)

    def pointers(self):
        def callback(e):
            x = e.x
            y = e.y
            print("Pointer is currently at %d, %d" % (x, y))

        self.bind('<Motion>', callback)

    def createHUD(self):
        self.teamImage()
        self.teamTitles()
        self.pitDisplay()
        self.makeDrops()
        # self.pointers()
        self.makeEntry()
        self.mainloop()
