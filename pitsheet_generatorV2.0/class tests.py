from tkinter import *
import constants


root = Tk()

root.title('Ronnies pitsheet')

xmax = 1035
ymax = 800

inkConservationMode = False

root.geometry(f'{xmax}x{ymax}')

canvas = Canvas(root, width=xmax, height=ymax)
canvas.pack()

def pointers():
    def callback(e):
        x = e.x
        y = e.y
        print("Pointer is currently at %d, %d" % (x, y))

    root.bind('<Motion>', callback)


# print bg

canvas.create_rectangle(0, 0, xmax, ymax, fill='white')


def bases(padding, segmentHeight, segmentWidth, segmentPadding, topPadding, offset, teamBoxOffsetx, teamBoxOffsety,
          teamBoxInitOffsetY, teamBoxHeight, teamBoxWidth, teamBoxItY, color, color2):
    # background
    if inkConservationMode == False:
        canvas.create_rectangle(0 + padding + offset, 0 + padding,
                                segmentWidth + (segmentPadding * 2) + padding + offset,
                                topPadding + ((segmentHeight + segmentPadding) * 3), fill=color)

    # team box bases
    for i in range(3):
        canvas.create_rectangle(padding + segmentPadding + offset, ((segmentHeight + segmentPadding) * i) + topPadding,
                                padding + segmentPadding + segmentWidth + offset,
                                ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight, fill=color2)

        canvas.create_rectangle(padding + segmentPadding + offset + 90,
                                ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 30,
                                padding + segmentPadding + 135 + offset,
                                ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight, fill=color)

    # team background data bases (sorry)
    for y in range(4):

        for i in range(3):

            for x in range(3):
                canvas.create_rectangle(padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x), ((
                                                                                                                          segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                                y * teamBoxItY),
                                        padding + segmentPadding + offset + teamBoxOffsetx + teamBoxWidth + (
                                                teamBoxWidth * x), ((
                                                                            segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + teamBoxHeight + (
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

            canvas.create_text(
                padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY - (
                        teamBoxHeight / 2), text=localtext, font=(10))

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

            canvas.create_text(padding + segmentPadding + offset + teamBoxOffsetx - 30, (
                    (segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                                       y * teamBoxItY) + (teamBoxHeight / 2), text=localtext, font=(10))


# def gameCalc():

def bars(color, color2, teamDat):
    localPlaceholder = 200
    canvas.create_rectangle(310, 200, 310 + teamDat["Auton Points Blue"], 175, fill=color)
    canvas.create_text(700, 177, text=teamDat["Auton Points Blue"], font=('Arial', 15))

    canvas.create_rectangle(310, 210, 310 + teamDat["Auton Points Red"], 235, fill=color2)
    canvas.create_text(700, 222.5, text=teamDat["Auton Points Red"], font=('Arial', 15))

    canvas.create_text(517.5, 145, text='Auton Points', font=('Arial', 15))

    canvas.create_rectangle(310, 200 + 150, 310 + teamDat["Teleop Cubes Blue"], 175 + 150, fill=color)
    canvas.create_text(700, 177 + 150, text=teamDat["Teleop Cubes Blue"], font=('Arial', 15))

    canvas.create_rectangle(310, 210 + 150, 310 + teamDat["Teleop Cubes Red"], 235 + 150, fill=color2)
    canvas.create_text(700, 222.5 + 150, text=teamDat["Teleop Cubes Red"], font=('Arial', 15))

    canvas.create_text(517.5, 145 + 150, text='Teleop Cubes', font=('Arial', 15))

    canvas.create_rectangle(310, 200 + 300, 310 + teamDat["Teleop Cones Blue"], 175 + 300, fill=color)
    canvas.create_text(700, 177 + 300, text=teamDat["Teleop Cones Blue"], font=('Arial', 15))

    canvas.create_rectangle(310, 210 + 300, 310 + teamDat["Teleop Cones Red"], 235 + 300, fill=color2)
    canvas.create_text(700, 222.5 + 300, text=teamDat["Teleop Cones Red"], font=('Arial', 15))

    canvas.create_text(517.5, 145 + 300, text='Teleop Cones', font=('Arial', 15))

    canvas.create_rectangle(310, 200 + 450, 310 + teamDat["Endgame Blue"], 175 + 450, fill=color)
    canvas.create_text(700, 177 + 450, text=teamDat["Endgame Blue"], font=('Arial', 15))

    canvas.create_rectangle(310, 210 + 450, 310 + teamDat["Endgame Red"], 235 + 450, fill=color2)
    canvas.create_text(700, 222.5 + 450, text=teamDat["Endgame Red"], font=('Arial', 15))

    canvas.create_text(517.5, 145 + 450, text='Endgame', font=('Arial', 15))


def teamcard(padding, segmentHeight, segmentWidth, segmentPadding, topPadding, offset, teamBoxOffsetx, teamBoxOffsety,
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
                canvas.create_text(
                    padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                    ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                            y * teamBoxItY) + (teamBoxHeight / 2), text=f'{teamDict[f"{firstString}{secondString}"]}{percent}',
                    font=('Arial', 12))

    for i in range(3):
        canvas.create_text(padding + segmentPadding + offset + 112.5,
                           ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 15,
                           text=teamNums[i], font=('Arial', 12))


def totalCalc(teams, type):
    a = 0
    for j in range(3):
        for k in range(4):
            a += makeDict(teams[j])[f'{constants.prefixes[k]}{type}']

    return a

def scorePredictor(teams):
    totalCalc(teams[0], 'Low')

    canvas.create_rectangle(300, 70, 400, 100, fill='#42e3f5')
    canvas.create_text(350, 85, text=f"{totalCalc(teams[0], 'Low')}|{totalCalc(teams[0], 'Avg')}|{totalCalc(teams[0], 'High')}",
                       font=('Arial', 15))

    canvas.create_rectangle(620, 70, 720, 100, fill='red')
    canvas.create_text(670, 85, text=f"{totalCalc(teams[1], 'Low')}|{totalCalc(teams[0], 'Avg')}|{totalCalc(teams[0], 'High')}",
                       font=('Arial', 15))


def main(teams, matchNumber):
    matchData = {
        "Auton Points Blue": makeDict(teams[0][0])['Auton Point Avg'] + makeDict(teams[0][1])['Auton Point Avg'] +
                             makeDict(teams[0][2])['Auton Point Avg'],
        "Teleop Cubes Blue": makeDict(teams[0][0])['Teleop Cubes Avg'] + makeDict(teams[0][1])['Teleop Cubes Avg'] +
                             makeDict(teams[0][2])['Teleop Cubes Avg'],
        "Teleop Cones Blue": makeDict(teams[0][0])['Teleop Cones Avg'] + makeDict(teams[0][1])['Teleop Cones Avg'] +
                             makeDict(teams[0][2])['Teleop Cones Avg'],
        "Endgame Blue": makeDict(teams[0][0])['Endgame Point Avg'] + makeDict(teams[0][1])['Endgame Point Avg'] +
                        makeDict(teams[0][2])['Endgame Point Avg'],
        "Auton Points Red": makeDict(teams[1][0])['Auton Point Avg'] + makeDict(teams[1][1])['Auton Point Avg'] +
                            makeDict(teams[1][2])['Auton Point Avg'],
        "Teleop Cubes Red": makeDict(teams[1][0])['Teleop Cubes Avg'] + makeDict(teams[1][1])['Teleop Cubes Avg'] +
                            makeDict(teams[1][2])['Teleop Cubes Avg'],
        "Teleop Cones Red": makeDict(teams[1][0])['Teleop Cones Avg'] + makeDict(teams[1][1])['Teleop Cones Avg'] +
                            makeDict(teams[1][2])['Teleop Cones Avg'],
        "Endgame Red": makeDict(teams[1][0])['Endgame Point Avg'] + makeDict(teams[1][1])['Endgame Point Avg'] +
                       makeDict(teams[1][2])['Endgame Point Avg']}

    canvas.create_text(517.5, 70, text=f'Match {matchNumber}', font=('Arial', 20))

    # blue
    bases(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5')

    teamcard(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', teams[0])

    # red
    bases(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#ffaaab', 'red')

    teamcard(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', teams[1])

    bars('#42e3f5', 'red', matchData)

    scorePredictor(teams)


nums = [[1481, 1481, 1481], [1481, 1481, 1481]]

main(nums, 10)

root.mainloop()
