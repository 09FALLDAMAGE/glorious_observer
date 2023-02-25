import tkinter as tk
from tkinter import Canvas

import errorHandeler
from errorHandeler import *
from jsonInterpreter import *
from constants import *


class generatePitSheet(tk.Tk):
    def __init__(self, mN, BtNS, RtNS):
        super(generatePitSheet, self).__init__()

        self.geo = [1035, 800]

        self.inkConservationMode = False

        self.title(f"Ronnie's Pit sheet V{constants.version}")

        self.geometry(f"{self.geo[0]}x{self.geo[1]}")
        self.canvas = Canvas(self, width=self.geo[0], height=self.geo[1])
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, self.geo[0], self.geo[1], fill='white')

        self.matchNumber = mN

        self.bTeams = BtNS

        self.rTeams = RtNS

        self.B1 = makeDict(BtNS[0])

        self.B2 = makeDict(BtNS[1])

        self.B3 = makeDict(BtNS[2])

        self.R1 = makeDict(RtNS[0])

        self.R2 = makeDict(RtNS[1])

        self.R3 = makeDict(RtNS[2])


    def bases(self, padding, segmentHeight, segmentWidth, segmentPadding, topPadding, offset, teamBoxOffsetx,
              teamBoxOffsety,
              teamBoxInitOffsetY, teamBoxHeight, teamBoxWidth, teamBoxItY, color, color2):
        # background
        if not self.inkConservationMode:
            self.canvas.create_rectangle(0 + padding + offset, 0 + padding,
                                         segmentWidth + (segmentPadding * 2) + padding + offset,
                                         topPadding + ((segmentHeight + segmentPadding) * 3), fill=color)

        # team box bases
        for i in range(3):
            self.canvas.create_rectangle(padding + segmentPadding + offset,
                                         ((segmentHeight + segmentPadding) * i) + topPadding,
                                         padding + segmentPadding + segmentWidth + offset,
                                         ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight,
                                         fill=color2)

            self.canvas.create_rectangle(padding + segmentPadding + offset + 90,
                                         ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 30,
                                         padding + segmentPadding + 135 + offset,
                                         ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight,
                                         fill=color)

        # team background data bases (sorry)
        for y in range(4):

            for i in range(3):

                for x in range(3):
                    self.canvas.create_rectangle(
                        padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x),
                        ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                y * teamBoxItY),
                        padding + segmentPadding + offset + teamBoxOffsetx + teamBoxWidth + (
                                teamBoxWidth * x),
                        ((segmentHeight + segmentPadding) * i) + topPadding +
                        teamBoxOffsety + teamBoxInitOffsetY + teamBoxHeight + (
                                y * teamBoxItY),
                        fill=color)

        # top titles
        for i in range(3):

            for x in range(3):
                if (x == 0):
                    localtext = 'Min'
                elif (x == 1):
                    localtext = 'Mean'
                elif (x == 2):
                    localtext = 'Max'

                self.canvas.create_text(
                    padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                    ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY - (
                            teamBoxHeight / 2), text=localtext, font=('Arial', 13))

        for y in range(4):

            for i in range(3):
                if (y == 0):
                    localtext = 'Auton'
                elif (y == 1):
                    localtext = 'Cones'
                elif (y == 2):
                    localtext = 'Cubes'
                elif (y == 3):
                    localtext = 'End'

                self.canvas.create_text(padding + segmentPadding + offset + teamBoxOffsetx - 30, (
                        (segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                                y * teamBoxItY) + (teamBoxHeight / 2), text=localtext, font=(10))

    # def gameCalc():

    def bars(self, color, color2, teamDat):
        self.canvas.create_rectangle(310, 200, 310 + (teamDat["Auton Points Blue"] * constants.barMult), 175, fill=color)
        self.canvas.create_text(700, 177, text=teamDat["Auton Points Blue"], font=('Arial', 15))

        self.canvas.create_rectangle(310, 210, 310 + (teamDat["Auton Points Red"] * constants.barMult), 235, fill=color2)
        self.canvas.create_text(700, 222.5, text=teamDat["Auton Points Red"], font=('Arial', 15))

        self.canvas.create_text(517.5, 145, text='Auton Points', font=('Arial', 15))

        self.canvas.create_rectangle(310, 200 + 150, 310 + (teamDat["Teleop Cubes Blue"] * constants.barMult), 175 + 150, fill=color)
        self.canvas.create_text(700, 177 + 150, text=teamDat["Teleop Cubes Blue"], font=('Arial', 15))

        self.canvas.create_rectangle(310, 210 + 150, 310 + (teamDat["Teleop Cubes Red"] * constants.barMult), 235 + 150, fill=color2)
        self.canvas.create_text(700, 222.5 + 150, text=teamDat["Teleop Cubes Red"], font=('Arial', 15))

        self.canvas.create_text(517.5, 145 + 150, text='Teleop Cubes', font=('Arial', 15))

        self.canvas.create_rectangle(310, 200 + 300, 310 + (teamDat["Teleop Cones Blue"] * constants.barMult), 175 + 300, fill=color)
        self.canvas.create_text(700, 177 + 300, text=teamDat["Teleop Cones Blue"], font=('Arial', 15))

        self.canvas.create_rectangle(310, 210 + 300, 310 + (teamDat["Teleop Cones Red"] * constants.barMult), 235 + 300, fill=color2)
        self.canvas.create_text(700, 222.5 + 300, text=teamDat["Teleop Cones Red"], font=('Arial', 15))

        self.canvas.create_text(517.5, 145 + 300, text='Teleop Cones', font=('Arial', 15))

        self.canvas.create_rectangle(310, 200 + 450, 310 + (teamDat["Endgame Blue"] * constants.barMult), 175 + 450, fill=color)
        self.canvas.create_text(700, 177 + 450, text=teamDat["Endgame Blue"], font=('Arial', 15))

        self.canvas.create_rectangle(310, 210 + 450, 310 + (teamDat["Endgame Red"] * constants.barMult), 235 + 450, fill=color2)
        self.canvas.create_text(700, 222.5 + 450, text=teamDat["Endgame Red"], font=('Arial', 15))

        self.canvas.create_text(517.5, 145 + 450, text='Endgame', font=('Arial', 15))


    def teamcard(self, padding, segmentHeight, segmentWidth, segmentPadding, topPadding, offset, teamBoxOffsetx,
                 teamBoxOffsety,
                 teamBoxInitOffsetY, teamBoxHeight, teamBoxWidth, teamBoxItY, color, color2, teamNums):
        makeDict(teamNums)
        for y in range(4):
            firstString = constants.prefixes[y]
            for i in range(3):
                teamDict = makeDict(teamNums[i])

                for x in range(3):
                    secondString = constants.suffixes[x]

                    if y == 0:
                        percent = '%'
                    elif y == 3:
                        percent = '%'
                    else:
                        percent = ''
                    self.canvas.create_text(
                        padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                        ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                y * teamBoxItY) + (teamBoxHeight / 2),
                        text=f'{teamDict[f"{firstString}{secondString}"]}{percent}',
                        font=('Arial', 12))

        for i in range(3):
            self.canvas.create_text(padding + segmentPadding + offset + 112.5,
                                    ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 15,
                                    text=teamNums[i], font=('Arial', 12))

    def totalCalc(self, teams, code):
        try:
            a = 0
            for j in range(3):
                for k in range(4):
                    a += makeDict(teams[j])[f'{constants.prefixes[k]}{code}']

            return a
        except:
            errorUpdate(1, "NO TEAM DATA")

    def scorePredictor(self, teams):
        self.totalCalc(teams[0], 'Low')

        self.canvas.create_rectangle(300, 70, 400, 100, fill='#42e3f5')
        self.canvas.create_text(350, 85,
                                text=f"{self.totalCalc(teams[0], 'Low')}|{self.totalCalc(teams[0], 'Avg')}|{self.totalCalc(teams[0], 'High')}",
                                font=('Arial', 15))

        self.canvas.create_rectangle(620, 70, 720, 100, fill='red')
        self.canvas.create_text(670, 85,
                                text=f"{self.totalCalc(teams[1], 'Low')}|{self.totalCalc(teams[0], 'Avg')}|{self.totalCalc(teams[0], 'High')}",
                                font=('Arial', 15))

    def generateSheet(self):
        matchData = {
            "Auton Points Blue": self.B1['Auton Point Avg'] + self.B2['Auton Point Avg'] + self.B3['Auton Point Avg'],
            "Teleop Cubes Blue": self.B1['Teleop Cubes Avg'] + self.B2['Teleop Cubes Avg'] + self.B3[
                'Teleop Cubes Avg'],
            "Teleop Cones Blue": self.B1['Teleop Cones Avg'] + self.B2['Teleop Cones Avg'] + self.B3[
                'Teleop Cones Avg'],
            "Endgame Blue": self.B1['Endgame Point Avg'] + self.B2['Endgame Point Avg'] + self.B3['Endgame Point Avg'],
            "Auton Points Red": self.R1['Auton Point Avg'] + self.R2['Auton Point Avg'] + self.R3['Auton Point Avg'],
            "Teleop Cubes Red": self.R1['Teleop Cubes Avg'] + self.R2['Teleop Cubes Avg'] + self.R3['Teleop Cubes Avg'],
            "Teleop Cones Red": self.R1['Teleop Cones Avg'] + self.R2['Teleop Cones Avg'] + self.R3['Teleop Cones Avg'],
            "Endgame Red": self.R1['Endgame Point Avg'] + self.R2['Endgame Point Avg'] + self.R3['Endgame Point Avg']}

        self.canvas.create_text(517.5, 70, text=f'Match {self.matchNumber}', font=('Arial', 20))

        # blue
        self.bases(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5')

        self.teamcard(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', self.bTeams)

        # red
        self.bases(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#ffaaab', 'red')

        self.teamcard(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', self.rTeams)

        self.bars('#42e3f5', 'red', matchData)

        self.scorePredictor([self.bTeams, self.rTeams])

        self.mainloop()

        # if errorHandeler.errorCheck():
        #     self.mainloop()
        # else:
        #     self.destroy()
        #     errorHandeler.returnWarning('Killed Pit sheet')

