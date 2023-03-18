import random
import tkinter as tk
from tkinter import Canvas
import os
import time
import win32api

from errorHandeler import errorUpdate
from constants import *
from jsonInterpreter import makeDict, autonAvg

import io
from dataTables import dataTables
import interface
import ghostscript


class generatePitSheet(tk.Tk):
    def __init__(self, mN, BtNS, RtNS):
        super(generatePitSheet, self).__init__()

        self.printername = 'http://[fe80::ba:d0ff:fe8f:1e3d%7]:3911/'

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

        try:
            os.remove('the.png')
            os.remove('the.ps')
        except:
            filler = 1

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
        for y in range(5):

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
                            teamBoxHeight / 2), text=localtext, font=('Arial', '13'))

        for y in range(5):

            for i in range(3):
                if (y == 0):
                    localtext = 'A Cone'
                elif (y == 1):
                    localtext = 'A Cube'
                elif (y == 2):
                    localtext = 'Cones'
                elif (y == 3):
                    localtext = 'Cubes'
                elif (y == 4):
                    localtext = 'End'

                self.canvas.create_text(padding + segmentPadding + offset + teamBoxOffsetx - 30, (
                        (segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                                y * teamBoxItY) + (teamBoxHeight / 2), text=localtext,
                                        font=('Arial', '12'))

    # def gameCalc():

    def bars(self, color, color2, teamDat):
        self.canvas.create_rectangle(310, 200, 310 + (teamDat["Auton Points Blue"] * constants.barMult), 175,
                                     fill=color)
        self.canvas.create_text(700, 177, text=teamDat["Auton Points Blue"], font=('Arial', '15'))

        self.canvas.create_rectangle(310, 210, 310 + (teamDat["Auton Points Red"] * constants.barMult), 235,
                                     fill=color2)
        self.canvas.create_text(700, 222.5, text=teamDat["Auton Points Red"], font=('Arial', '15'))

        self.canvas.create_text(517.5, 145, text='Auton Points', font=('Arial', '15'))

        self.canvas.create_rectangle(310, 200 + 150, 310 + (teamDat["Teleop Cubes Blue"] * constants.barMult),
                                     175 + 150, fill=color)
        self.canvas.create_text(700, 177 + 150, text=teamDat["Teleop Cubes Blue"], font=('Arial', '15'))

        self.canvas.create_rectangle(310, 210 + 150, 310 + (teamDat["Teleop Cubes Red"] * constants.barMult), 235 + 150,
                                     fill=color2)
        self.canvas.create_text(700, 222.5 + 150, text=teamDat["Teleop Cubes Red"], font=('Arial', '15'))

        self.canvas.create_text(517.5, 145 + 150, text='Teleop Cubes', font=('Arial', 15))

        self.canvas.create_rectangle(310, 200 + 300, 310 + (teamDat["Teleop Cones Blue"] * constants.barMult),
                                     175 + 300, fill=color)
        self.canvas.create_text(700, 177 + 300, text=teamDat["Teleop Cones Blue"], font=('Arial', '15'))

        self.canvas.create_rectangle(310, 210 + 300, 310 + (teamDat["Teleop Cones Red"] * constants.barMult), 235 + 300,
                                     fill=color2)
        self.canvas.create_text(700, 222.5 + 300, text=teamDat["Teleop Cones Red"], font=('Arial', '15'))

        self.canvas.create_text(517.5, 145 + 300, text='Teleop Cones', font=('Arial', '15'))

        self.canvas.create_rectangle(310, 200 + 450, 310 + (teamDat["Endgame Blue"] * constants.barMult), 175 + 450,
                                     fill=color)
        self.canvas.create_text(700, 177 + 450, text=teamDat["Endgame Blue"], font=('Arial', '15'))

        self.canvas.create_rectangle(310, 210 + 450, 310 + (teamDat["Endgame Red"] * constants.barMult), 235 + 450,
                                     fill=color2)
        self.canvas.create_text(700, 222.5 + 450, text=teamDat["Endgame Red"], font=('Arial', '15'))

        self.canvas.create_text(517.5, 145 + 450, text='Endgame', font=('Arial', '15'))

    def teamcard(self, padding, segmentHeight, segmentWidth, segmentPadding, topPadding, offset, teamBoxOffsetx,
                 teamBoxOffsety,
                 teamBoxInitOffsetY, teamBoxHeight, teamBoxWidth, teamBoxItY, color, color2, teamNums):
        for y in range(5):
            firstString = constants.prefixes[y]
            for i in range(3):
                teamDict = makeDict(teamNums[i])

                for x in range(3):
                    secondString = constants.suffixes[x]

                    if y == 0:
                        percent = ''
                    elif y == 3:
                        percent = ''
                    else:
                        percent = ''
                    self.canvas.create_text(
                        padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                        ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                y * teamBoxItY) + (teamBoxHeight / 2),
                        text=round(teamDict[f"{constants.prefixes[y]}{constants.suffixes[x]}"]),
                        font=('Arial', '12'))

        for i in range(3):
            self.canvas.create_text(padding + segmentPadding + offset + 112.5,
                                    ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 15,
                                    text=teamNums[i], font=('Arial', '12'))
            teamDict = makeDict(teamNums[i])
            for j in range(2):
                self.canvas.create_text(padding + segmentPadding + offset + 45 + (135 * j),
                                        ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 30,
                                        text='None, Dock, Eng',
                                        font=('Arial', '8'))
                for k in range(3):
                    # print(f"{constants.percentPrefix[j]}{constants.percentSuff[k]}Percent")
                    # print(teamDict[f"{constants.percentPrefix[j]}{constants.percentSuff[k]}Percent"])
                    # print(autonAvg(teamNums[i])[3 + k])
                    self.canvas.create_text(padding + segmentPadding + offset + 20 + (132 * j) + (28 * k),
                                            ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 15,
                                            text=f'{round((teamDict[f"{constants.percentPrefix[j]}{constants.percentSuff[k]}Percent"] * 100))}%',
                                            font=('Arial', '8'))

    def totalCalc(self, teams, code):
        try:
            a = 0
            for j in range(3):
                for k in range(4):
                    a += round(makeDict(teams[j])[f'{constants.totalPrefixes[k]}{code}'])

            return a
        except:
            errorUpdate(1, "NO TEAM DATA")

    def scorePredictor(self, bTeams, rTeams):

        self.canvas.create_rectangle(300, 70, 400, 100, fill='#42e3f5')
        # blue
        self.canvas.create_text(350, 85,
                                text=f"{self.totalCalc(bTeams, 'Low')}|{self.totalCalc(bTeams, 'Avg')}|{self.totalCalc(bTeams, 'High')}",
                                font=('Arial', '15'))

        self.canvas.create_rectangle(620, 70, 720, 100, fill='red')
        # red
        self.canvas.create_text(670, 85,
                                text=f"{self.totalCalc(rTeams, 'Low')}|{self.totalCalc(rTeams, 'Avg')}|{self.totalCalc(rTeams, 'High')}",
                                font=('Arial', '15'))

    def generateSheet(self):
        # interface.interface().loadingBar(1)
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
        # interface.interface().loadingBar(10)
        self.canvas.create_text(517.5, 70, text=f'Match {self.matchNumber.upper()}', font=('Arial', '20'))
        # interface.interface().loadingBar(11)
        # blue
        self.bases(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 30, '#add8e6', '#42e3f5')
        # interface.interface().loadingBar(13)
        self.teamcard(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 30, '#add8e6', '#42e3f5', self.bTeams)
        # interface.interface().loadingBar(15)
        # red
        self.bases(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 30, '#ffaaab', 'red')
        # interface.interface().loadingBar(17)
        self.teamcard(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 30, '#add8e6', '#42e3f5', self.rTeams)
        # interface.interface().loadingBar(18)
        self.bars('#42e3f5', 'red', matchData)
        # interface.interface().loadingBar(20)
        self.scorePredictor(self.bTeams, self.rTeams)
        # interface.interface().loadingBar(24)
        self.canvas.postscript(colormode='color', x=0, y=0, height=self.geo[1], width=self.geo[0], file='the.ps')

        from PIL import Image as balls

        psimage = balls.open('the.ps')
        psimage.save('the.jpeg')
        # os.startfile('the.ps', "print")

        self.mainloop()

        # if errorHandeler.errorCheck():
        #     self.mainloop()
        # else:
        #     self.destroy()
        #     errorHandeler.returnWarning('Killed Pit sheet')
