from constants import *
import json
import time

start = time.time()

fileopen = open(constants.jsonName)
jsonData = json.loads(fileopen.read())
names = jsonData.keys()
fileopen.close()


def getData(teamNumber, dataName):
    # turns the json file into a dictionary the python can interact with
    total = []
    # creates a blank array for total (I'm still not exactly sure what total does anymore, I think it gets an array of the values or soemthing)

    maxMatches = 100
    # set the maximum matches

    for i in range(1, maxMatches):
        teamMatchAndNumber = f"{i}_{teamNumber}"
        if (teamMatchAndNumber in names):
            valueNames = jsonData[teamMatchAndNumber].keys()
            if (dataName in valueNames):
                total.append(int(jsonData[teamMatchAndNumber][dataName]))
            else:
                print(valueNames)
                print("you failed, try again, idk")
                return 0
    # appends the value(s) of a chosen data type into an array for usage later

    return total
    # returns the array total to the function


def getDataStr(teamNumber, dataName):
    # does the exact same thing as the previous one but this time it's for string values not integer values

    total = []

    maxMatches = 100

    for i in range(maxMatches):
        teamMatchAndNumber = f"{i}_{teamNumber}"
        if (teamMatchAndNumber in names):
            valueNames = jsonData[teamMatchAndNumber].keys()
            if (dataName in valueNames):
                total.append(str(jsonData[teamMatchAndNumber][dataName]))
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

    autonPercents = []
    # dont worry about it

    autonBalanceChargeStation = (getDataStr(teamNumber, "Autonomous End Of Auton Pos"))
    # creates a useable array for "Autonomous Balance Charging Station" data

    autonPercents.append(float(autonBalanceChargeStation.count("Nothing") / length))
    autonPercents.append(float(autonBalanceChargeStation.count("Docked") / length))
    autonPercents.append(float(autonBalanceChargeStation.count("Engaged") / length))
    # autonPercents = [int(autonBalanceChargeStation.count("Nothing") / length), int(autonBalanceChargeStation.count("Docked") / length), int(autonBalanceChargeStation.count("Engaged") / length)]
    autonCrossLine = (getDataStr(teamNumber, "Autonomous Cross Line"))
    # creates a useable array for "Autonomous Leave Community" data

    for i in range(0, length):
        if autonBalanceChargeStation[i] == 'Nothing':
            autonBalanceChargeStation[i] = 0
        elif autonBalanceChargeStation[i] == 'Docked':
            autonBalanceChargeStation[i] = 2
        elif autonBalanceChargeStation[i] == 'Engaged':
            autonBalanceChargeStation[i] = 3
        # changing the string values of "Autonomous Balance Charging Station" into numerical values
        if (autonCrossLine[i] == 'false'):
            autonCrossLine[i] = 0
        elif (autonCrossLine[i] == 'true'):
            autonCrossLine[i] = 1
    # changing the string values of "Autonomous Leave Community" into numerical values

    for i in range(1, length + 1):
        balancePointA = autonBalanceChargeStation[length - i] * 4
        # calculate points from balancing charging station in auton

        leaveCommA = autonCrossLine[length - i] * 3
        # calculate points from leaving the community in auton
        cubePointA = (getData(teamNumber, "Autonomous High Cubes")[length - i] * constants.x) + (
                getData(teamNumber, "Autonomous Med Cubes")[length - i] * constants.y) + (
                             getData(teamNumber, "Autonomous Low Cubes")[length - i] * constants.z)
        # calculates the points scored from cubes in auton
        cubesScoredNumA = (getData(teamNumber, "Autonomous High Cubes")[length - i]) + (
            getData(teamNumber, "Autonomous Med Cubes")[length - i]) + (
                              getData(teamNumber, "Autonomous Low Cubes")[length - i])
        cubesScoredA += cubesScoredNumA
        cubeAvgA = cubePointA / length
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
        coneAvgA = conePointA / length
        # calculates average number of cones scored by a team in auton
        coneHighLowA.append(int(conePointA))
        coneHighLowA.sort()
        # appends and sorts a list full of cone score values
        autonTotal += cubePointA + conePointA + balancePointA + leaveCommA
        autonAvg = int(round(autonTotal / length, 0))
        # calculates the total points scored in auton and their average
        autonRoundTotal = cubePointA + conePointA + balancePointA + leaveCommA
        autonHighLow.append(int(autonRoundTotal))
        autonHighLow.sort()
        # appends and sorts a list of auton match scores
    print(cubeHighLowA)
    cubeMinA = min(cubeHighLowA)
    cubeMaxA = max(cubeHighLowA)
    # gets the lowest and highest values of cube points scored out of played matches (auton)

    coneMinA = coneHighLowA[0]
    coneMaxA = coneHighLowA[len(coneHighLowA) - 1]
    # gets the lowest and highest values of cone points scored out of played matches (auton)

    autonMin = autonHighLow[0]
    autonMax = autonHighLow[len(autonHighLow) - 1]
    # gets the lowest and highest scores during auton from played matches

    autoList = [autonMin, autonAvg, autonMax, autonPercents[0], autonPercents[1], autonPercents[2], cubeMinA, cubeAvgA,
                cubeMaxA, coneMinA, coneAvgA, coneMaxA]
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

    endgamePercents = []

    endgameEndPos = (getDataStr(teamNumber, "Endgame Ending Position"))

    endgamePercents.append(float(endgameEndPos.count("Nothing") / length))
    endgamePercents.append(float(endgameEndPos.count("Docked") / length))
    endgamePercents.append(float(endgameEndPos.count("Engaged") / length))

    for i in range(0, length):
        if (endgameEndPos[i] == 'Nothing'):
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
    # print(endgamePercents)

    endgameBalanceTimeAvg = 0
    # declares variable for getting endgame balance time average later

    return [endgameMin, endgameAverage, endgameMax, endgamePercents[0], endgamePercents[1], endgamePercents[2]]

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
        team1["Auton None Percent"] = autonAvg(teamNumber)[3]
        team1["Auton Docked Percent"] = autonAvg(teamNumber)[4]
        team1["Auton Engaged Percent"] = autonAvg(teamNumber)[5]
        team1["Auton Cubes Low"] = autonAvg(teamNumber)[6]
        team1["Auton Cubes Avg"] = autonAvg(teamNumber)[7]
        team1["Auton Cubes High"] = autonAvg(teamNumber)[8]
        team1["Auton Cones Low"] = autonAvg(teamNumber)[9]
        team1["Auton Cones Avg"] = autonAvg(teamNumber)[10]
        team1["Auton Cones High"] = autonAvg(teamNumber)[11]
        team1["Teleop Cubes Low"] = teleopAvg(teamNumber)[0]
        team1["Teleop Cubes Avg"] = teleopAvg(teamNumber)[1]
        team1["Teleop Cubes High"] = teleopAvg(teamNumber)[2]
        team1["Teleop Cones Low"] = teleopAvg(teamNumber)[3]
        team1["Teleop Cones Avg"] = teleopAvg(teamNumber)[4]
        team1["Teleop Cones High"] = teleopAvg(teamNumber)[5]
        team1["Endgame Point Low"] = endgameAvg(teamNumber)[0]
        team1["Endgame Point Avg"] = endgameAvg(teamNumber)[1]
        team1["Endgame Point High"] = endgameAvg(teamNumber)[2]
        team1["Endgame None Percent"] = endgameAvg(teamNumber)[3]
        team1["Endgame Docked Percent"] = endgameAvg(teamNumber)[4]
        team1["Endgame Engaged Percent"] = endgameAvg(teamNumber)[5]
        # populates the dictionary team1

        return team1
    except:
        team1 = {}
        # creates dictionary team1
        team1["Auton Point Low"] = "null"
        team1["Auton Point Avg"] = "null"
        team1["Auton Point High"] = "null"
        team1["Auton Nothing Percent"] = "null"
        team1["Auton Docked Percent"] = "null"
        team1["Auton Engaged Percent"] = "null"
        team1["Teleop Cubes Low"] = "null"
        team1["Teleop Cubes Avg"] = "null"
        team1["Teleop Cubes High"] = "null"
        team1["Teleop Cones Low"] = "null"
        team1["Teleop Cones Avg"] = "null"
        team1["Teleop Cones High"] = "null"
        team1["Endgame Point Low"] = "null"
        team1["Endgame Point Avg"] = "null"
        team1["Endgame Point High"] = "null"
        team1["Endgame Point High"] = "null"
        team1["Endgame None Percent"] = "null"
        team1["Endgame Docked Percent"] = "null"
        team1["Endgame Engaged Percent"] = "null"
        # populates the dictionary team1

        return team1
    # returns the dictionary team1 to makeDict


def printDict(teamNumber):
    print(makeDict(teamNumber))

print(makeDict(67))

end = time.time()
print(end - start)