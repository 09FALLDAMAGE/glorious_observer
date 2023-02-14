from tkinter import *
import json
import constants
import random

root = Tk()

root.title('Ronnies pitsheet')

xmax = 1035
ymax = 800

inkConservationMode = False

root.geometry(f'{xmax}x{ymax}')

canvas = Canvas(root, width=xmax, height=ymax)
canvas.pack()


def getData(teamNumber, dataName):
    tmpData = open(constants.jsonName)
    jsonFile = json.loads(tmpData.read())
    names = jsonFile.keys()
    # turns the json file into a dictionary the python can interact with
    total = []
    # creates a blank array for total (I'm still not exactly sure what total does anymore, I think it gets an array of the values or soemthing)

    maxMatches = 100
    # set the maximum matches

    for i in range(1, maxMatches):
        teamMatchAndNumber = f"{i}_{teamNumber}"
        if (teamMatchAndNumber in names):
            valueNames = jsonFile[teamMatchAndNumber].keys()
            if (dataName in valueNames):
                total.append(int(jsonFile[teamMatchAndNumber][dataName]))
            else:
                print(valueNames)
                print("you failed, try again, idk")
                return 0
    # appends the value(s) of a chosen data type into an array for usage later

    return total
    # returns the array total to the function


def getDataStr(teamNumber, dataName):
    # does the exact same thing as the previous one but this time it's for string values not integer values
    tmpData = open('json.json')
    jsonFile = json.loads(tmpData.read());
    names = jsonFile.keys()

    total = []

    maxMatches = 100

    for i in range(maxMatches):
        teamMatchAndNumber = f"{i}_{teamNumber}"
        if (teamMatchAndNumber in names):
            valueNames = jsonFile[teamMatchAndNumber].keys()
            if (dataName in valueNames):
                total.append(str(jsonFile[teamMatchAndNumber][dataName]))
            else:
                print(valueNames)
                print("you failed, try again, idk")
                return 0

    return total


def cleanData(teamNumber):
    global length
    length = len(getData(teamNumber, "Team Number"))
    # gets the number of matches a specified team has played

    autonAvg(teamNumber)
    # runs autonAvg function
    teleopAvg(teamNumber)
    # runs teleopAvg
    endgameAvg(teamNumber)
    # runs endgameAvg
    makeDict(teamNumber)
    # runs makeDict


def autonAvg(teamNumber):
    global autonTotal
    autonTotal = 0
    # creates autonTotal variable for calculations
    length = len(getData(teamNumber, "Team Number"))

    cubesScoredA = 0
    conesScoredA = 0
    # declaring variables for average cones and cubes scored in auton

    cubeHighLowA = []
    # declaring array for later use of high/low calculations

    coneHighLowA = []
    # declaring array for later us of high/low calculations

    autonHighLow = []
    # declaring array for later us of high/low calculations

    autonBalanceChargeStation = (getDataStr(teamNumber, "Autonomous End Of Auton Pos"))
    # creates a useable array for "Autonomous Balance Charging Station" data

    #    autonLeaveComm = (getDataStr(teamNumber, "Autonomous Leave Community"))
    # creates a useable array for "Autonomous Leave Community" data

    for i in range(0, length):
        if (autonBalanceChargeStation[i] == 'Nothing'):
            autonBalanceChargeStation[i] = 0
        elif (autonBalanceChargeStation[i] == 'Parked'):
            autonBalanceChargeStation[i] = 0.75
        elif (autonBalanceChargeStation[i] == 'Docked'):
            autonBalanceChargeStation[i] = 2
        elif (autonBalanceChargeStation[i] == 'Engaged'):
            autonBalanceChargeStation[i] = 3
        # changing the string values of "Autonomous Balance Charging Station" into numerical values

        # if (autonLeaveComm[i] == 'false'):
        #     autonLeaveComm[i] = 0
        # elif (autonLeaveComm[i] == 'true'):
        #     autonLeaveComm[i] = 0
        # changing the string values of "Autonomous Leave Community" into numerical values

    for i in range(1, length + 1):
        balancePointA = autonBalanceChargeStation[length - i] * 4
        # calculate points from balancing charging station in auton

        #        leaveCommA = autonLeaveComm[length-i] * 3
        # calculate points from leaving the community in auton

        cubePointA = (getData(teamNumber, "Autonomous High Cubes")[length - i] * constants.x) + (
                getData(teamNumber, "Autonomous Med Cubes")[length - i] * constants.y) + (
                             getData(teamNumber, "Autonomous Low Cubes")[length - i] * constants.z)
        # calculates the points scored from cubes in auton
        cubesScoredNumA = (getData(teamNumber, "Autonomous High Cubes")[length - i]) + (
            getData(teamNumber, "Autonomous Med Cubes")[length - i]) + (
                              getData(teamNumber, "Autonomous Low Cubes")[length - i])
        cubesScoredA += cubesScoredNumA
        cubeAvgA = cubesScoredA / length
        # calculates average number of cubes scored by a team in auton
        cubeHighLowA.append(int(cubePointA))
        cubeHighLowA.sort()
        # appends and sorts a list full of cube score values

        conePointA = (getData(teamNumber, "Autonomous High Cones")[length - i] * constants.x) + (
                getData(teamNumber, "Autonomous Med Cones")[length - i] * constants.y) + (
                             getData(teamNumber, "Autonomous Low Cones")[length - i] * constants.z)
        # calculates the points scored from cones in auton
        conesScoredNumA = (getData(teamNumber, "Autonomous High Cones")[length - i]) + (
            getData(teamNumber, "Autonomous Med Cones")[length - i]) + (
                              getData(teamNumber, "Autonomous Low Cones")[length - i])
        conesScoredA += conesScoredNumA
        coneAvgA = conesScoredA / length
        # calculates average number of cones scored by a team in auton
        coneHighLowA.append(int(conePointA))
        coneHighLowA.sort()
        # appends and sorts a list full of cone score values

        autonTotal += cubePointA + conePointA + balancePointA  # +leaveCommA
        autonAvg = int(round(autonTotal / length, 0))
        # calculates the total points scored in auton and their average
        autonRoundTotal = cubePointA + conePointA + balancePointA  # + leaveCommA
        autonHighLow.append(int(autonRoundTotal))
        autonHighLow.sort()
        # appends and sorts a list of auton match scores

    cubeMinA = cubeHighLowA[0]
    cubeMaxA = cubeHighLowA[len(cubeHighLowA) - 1]
    # gets the lowest and highest values of cube points scored out of played matches (auton)

    coneMinA = coneHighLowA[0]
    coneMaxA = coneHighLowA[len(coneHighLowA) - 1]
    # gets the lowest and highest values of cone points scored out of played matches (auton)

    autonMin = autonHighLow[0]
    autonMax = autonHighLow[len(autonHighLow) - 1]
    # gets the lowest and highest scores during auton from played matches

    autoList = [autonMin, autonAvg, autonMax]
    # create a list of values that need to be put in a dictionary

    return autoList
    # returns that list to function


def teleopAvg(teamNumber):
    global teleTotal
    teleopTotal = 0
    # creates a variable for points scored in teleop for later calculations
    cubesScoredT = 0
    conesScoredT = 0
    # declaring variables for average cones and cubes scored in teleop
    cubePointScoredT = 0
    conePointScoredT = 0
    length = len(getData(teamNumber, "Team Number"))

    cubeHighLowT = []
    # declaring array for later use of high/low calculations

    coneHighLowT = []
    # declaring array for later us of high/low calculations

    teleopHighLow = []
    # declaring array for later us of high/low calculations

    for i in range(1, length + 1):
        cubePointT = (getData(teamNumber, "Teleop High Cubes")[length - i] * constants.x1) + (
                getData(teamNumber, "Teleop Med Cubes")[length - i] * constants.y1) + (
                             getData(teamNumber, "Teleop Low Cubes")[length - i] * constants.z1)
        # calculates the points scored from cubes in teleop
        cubePointScoredT += cubePointT
        cubePointAvgT = int(round(cubePointScoredT / length, 0))

        cubesScoredNumT = (getData(teamNumber, "Teleop High Cubes")[length - i]) + (
            getData(teamNumber, "Teleop Med Cubes")[length - i]) + (getData(teamNumber, "Teleop Low Cubes")[length - i])
        cubesScoredT += cubesScoredNumT
        cubeAvgT = int(round(cubesScoredT / length, 0))
        # calculates average number of cubes scored by a team in teleop
        cubeHighLowT.append(int(cubePointT))
        cubeHighLowT.sort()
        # appends and sorts a list full of cube score values

        conePointT = (getData(teamNumber, "Teleop High Cones")[length - i] * constants.x1) + (
                getData(teamNumber, "Teleop Med Cones")[length - i] * constants.y1) + (
                             getData(teamNumber, "Teleop Low Cones")[length - i] * constants.z1)
        # calculates the points scored from cones in teleop
        conePointScoredT += conePointT
        conePointAvgT = int(round(conePointScoredT / length, 0))

        conesScoredNumT = (getData(teamNumber, "Teleop High Cones")[length - i]) + (
            getData(teamNumber, "Teleop Med Cones")[length - i]) + (getData(teamNumber, "Teleop Low Cones")[length - i])
        conesScoredT += conesScoredNumT
        coneAvgT = int(round(conesScoredT / length, 0))
        # calculates average number of cones scored by a team in teleop
        coneHighLowT.append(int(conePointT))
        coneHighLowT.sort()
        # appends and sorts a list full of cone score values

        teleopTotal += cubePointT + conePointT
        teleopAvg = int(round(teleopTotal / length, 0))
        # calculates the total points scored in teleop and their average
        teleopRoundTotal = cubePointT + conePointT
        teleopHighLow.append(int(teleopRoundTotal))
        teleopHighLow.sort()
        # appends and sorts a list of teleop match scores

    cubeMinT = cubeHighLowT[0]
    cubeMaxT = cubeHighLowT[len(cubeHighLowT) - 1]
    # gets the lowest and highest values of cube points scored out of played matches (teleop)

    coneMinT = coneHighLowT[0]
    coneMaxT = coneHighLowT[len(coneHighLowT) - 1]
    # gets the lowest and highest values of cone points scored out of played matches (teleop)

    teleopMin = teleopHighLow[0]
    teleopMax = teleopHighLow[len(teleopHighLow) - 1]
    # gets the lowest and highest scores during teleop from played matches

    teleopList = [cubeMinT, cubePointAvgT, cubeMaxT, coneMinT, conePointAvgT, coneMaxT]
    # create a list of values that need to be put in a dictionary

    return teleopList
    # returns that list to function


def endgameAvg(teamNumber):
    global endgameTotal
    endgameTotal = 0
    # creates a variable for total points in endgame for calculations
    length = len(getData(teamNumber, "Team Number"))

    endgameHighLow = []

    endgameEndPos = (getDataStr(teamNumber, "Endgame Ending Position"))

    for i in range(0, length):
        if (endgameEndPos[i] == 'None'):
            endgameEndPos[i] = 0
        elif (endgameEndPos[i] == 'Docked'):
            endgameEndPos[i] = 3
        elif (endgameEndPos[i] == 'Engaged'):
            endgameEndPos[i] = 5

        endgameHighLow.append(int(endgameEndPos[i] * 2))
        endgameHighLow.sort()

    endgameAverage = int(round(sum(endgameHighLow) / length, 0))

    endgameMin = endgameHighLow[0]
    endgameMax = endgameHighLow[len(endgameHighLow) - 1]
    # gets the lowest and highest scores during auton from played matches

    endgameBalanceTimeAvg = 0
    # declares variable for getting endgame balance time average later

    return [endgameMin, endgameAverage, endgameMax]

    # for i in range(1, length+1):
    #     endgameBalanceTimeAvg += (getData(teamNumber, "Endgame Time to Balance")[length - i])
    # endgameBalanceTimeAvg = int(round(endgameBalanceTimeAvg/length))
    # calculations for getting the average time to balance during endgame


def makeDict(teamNumber):
    try:
        team1 = {}
        # creates dictionary team1
        team1["Auton Point Low"] = autonAvg(teamNumber)[0]
        team1["Auton Point Avg"] = autonAvg(teamNumber)[1]
        team1["Auton Point High"] = autonAvg(teamNumber)[2]
        team1["Teleop Cubes Low"] = teleopAvg(teamNumber)[0]
        team1["Teleop Cubes Avg"] = teleopAvg(teamNumber)[1]
        team1["Teleop Cubes High"] = teleopAvg(teamNumber)[2]
        team1["Teleop Cones Low"] = teleopAvg(teamNumber)[3]
        team1["Teleop Cones Avg"] = teleopAvg(teamNumber)[4]
        team1["Teleop Cones High"] = teleopAvg(teamNumber)[5]
        team1["Endgame Point Low"] = endgameAvg(teamNumber)[0]
        team1["Endgame Point Avg"] = endgameAvg(teamNumber)[1]
        team1["Endgame Point High"] = endgameAvg(teamNumber)[2]
        # populates the dictionary team1

        return team1
    except:
        team1 = {}
        # creates dictionary team1
        team1["Auton Point Low"] = "null"
        team1["Auton Point Avg"] = "null"
        team1["Auton Point High"] = "null"
        team1["Teleop Cubes Low"] = "null"
        team1["Teleop Cubes Avg"] = "null"
        team1["Teleop Cubes High"] = "null"
        team1["Teleop Cones Low"] = "null"
        team1["Teleop Cones Avg"] = "null"
        team1["Teleop Cones High"] = "null"
        team1["Endgame Point Low"] = "null"
        team1["Endgame Point Avg"] = "null"
        team1["Endgame Point High"] = "null"
        # populates the dictionary team1

        return team1
    # returns the dictionary team1 to makeDict


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

        for i in range(3):

            for x in range(3):
                if y == 0:
                    percent = '%'
                elif y == 3:
                    percent = '%'
                else:
                    percent = ''
                canvas.create_text(
                    padding + segmentPadding + offset + teamBoxOffsetx + (teamBoxWidth * x) + (teamBoxWidth / 2),
                    ((segmentHeight + segmentPadding) * i) + topPadding + teamBoxOffsety + teamBoxInitOffsetY + (
                            y * teamBoxItY) + (teamBoxHeight / 2), text=f'{random.randint(0, 50)}{percent}',
                    font=('Arial', 12))

    for i in range(3):
        canvas.create_text(padding + segmentPadding + offset + 112.5,
                           ((segmentHeight + segmentPadding) * i) + topPadding + segmentHeight - 15,
                           text=random.randint(0, 9999), font=('Arial', 12))


def scorePredictor():
    canvas.create_rectangle(300, 70, 400, 100, fill='#42e3f5')
    canvas.create_text(350, 85, text=f'{random.randint(0, 100)}|{random.randint(0, 100)}|{random.randint(0, 100)}',
                       font=('Arial', 15))

    canvas.create_rectangle(620, 70, 720, 100, fill='red')
    canvas.create_text(670, 85, text=f'{random.randint(0, 100)}|{random.randint(0, 100)}|{random.randint(0, 100)}',
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

    teamcard(40, 225, 225, 10, 50, 0, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', teams)

    # red
    bases(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#ffaaab', 'red')

    teamcard(40, 225, 225, 10, 50, 700, 70, 20, 20, 20, 40, 40, '#add8e6', '#42e3f5', teams)

    bars('#42e3f5', 'red', matchData)

    scorePredictor()


nums = [[1481, 1481, 1481], [1481, 1481, 1481]]

main(nums, 10)

pointers()

root.mainloop()
