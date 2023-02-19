from errorHandeler import *
from constants import *
import json


class jsons:
    def __init__(self, tN):
        self.teamID = tN

    def getData(self, dataName):
        tmpData = open(constants.jsonName)
        jsonFile = json.loads(tmpData.read())
        names = jsonFile.keys()
        # turns the json file into a dictionary the python can interact with
        total = []
        # creates a blank array for total (I'm still not exactly sure what total does anymore, I think it gets an array of the values or soemthing)

        maxMatches = 100
        # set the maximum matches

        for i in range(1, maxMatches):
            teamMatchAndNumber = f"{i}_{self.teamID}"
            if teamMatchAndNumber in names:
                valueNames = jsonFile[teamMatchAndNumber].keys()
                if dataName in valueNames:
                    total.append(int(jsonFile[teamMatchAndNumber][dataName]))
                else:
                    print(valueNames)
                    errorUpdate(1, 'Possible wrong SCHEMA, try new json PATH')
                    return 0
        # appends the value(s) of a chosen data type into an array for usage later

        return total
        # returns the array total to the function

    def getDataStr(self, dataName):
        # does the exact same thing as the previous one but this time it's for string values not integer values
        tmpData = open(constants.jsonName)
        jsonFile = json.loads(tmpData.read())
        names = jsonFile.keys()

        total = []

        maxMatches = 100

        for i in range(maxMatches):
            teamMatchAndNumber = f"{i}_{self.teamID}"
            if teamMatchAndNumber in names:
                valueNames = jsonFile[teamMatchAndNumber].keys()
                if dataName in valueNames:
                    total.append(str(jsonFile[teamMatchAndNumber][dataName]))
                else:
                    print(valueNames)
                    print("you failed, try again, idk")
                    return 0

        return total

    def cleanData(self):
        global length
        length = len(self.getData(self.teamID, "Team Number"))
        # gets the number of matches a specified team has played

        self.autonAvg(self.teamID)
        # runs autonAvg function
        self.teleopAvg(self.teamID)
        # runs teleopAvg
        self.endgameAvg(self.teamID)
        # runs endgameAvg
        self.makeDict(self.teamID)
        # runs makeDict

    def autonAvg(self):
        global autonTotal
        autonTotal = 0
        # creates autonTotal variable for calculations
        length = len(self.getData(self.teamID, "Team Number"))

        cubesScoredA = 0
        conesScoredA = 0
        # declaring variables for average cones and cubes scored in auton

        cubeHighLowA = []
        # declaring array for later use of high/low calculations

        coneHighLowA = []
        # declaring array for later us of high/low calculations

        autonHighLow = []
        # declaring array for later us of high/low calculations

        autonBalanceChargeStation = (self.getDataStr(self.teamID, "Autonomous End Of Auton Pos"))
        # creates a useable array for "Autonomous Balance Charging Station" data

        #    autonLeaveComm = (getDataStr(self.teamID, "Autonomous Leave Community"))
        # creates a useable array for "Autonomous Leave Community" data

        for i in range(0, length):
            if autonBalanceChargeStation[i] == 'Nothing':
                autonBalanceChargeStation[i] = 0
            elif autonBalanceChargeStation[i] == 'Parked':
                autonBalanceChargeStation[i] = 0.75
            elif autonBalanceChargeStation[i] == 'Docked':
                autonBalanceChargeStation[i] = 2
            elif autonBalanceChargeStation[i] == 'Engaged':
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

            cubePointA = (self.getData(self.teamID, "Autonomous High Cubes")[length - i] * constants.x) + (
                    self.getData(self.teamID, "Autonomous Med Cubes")[length - i] * constants.y) + (
                                 self.getData(self.teamID, "Autonomous Low Cubes")[length - i] * constants.z)
            # calculates the points scored from cubes in auton
            cubesScoredNumA = (self.getData(self.teamID, "Autonomous High Cubes")[length - i]) + (
                self.getData(self.teamID, "Autonomous Med Cubes")[length - i]) + (
                                  self.getData(self.teamID, "Autonomous Low Cubes")[length - i])
            cubesScoredA += cubesScoredNumA
            cubeAvgA = cubesScoredA / length
            # calculates average number of cubes scored by a team in auton
            cubeHighLowA.append(int(cubePointA))
            cubeHighLowA.sort()
            # appends and sorts a list full of cube score values

            conePointA = (self.getData(self.teamID, "Autonomous High Cones")[length - i] * constants.x) + (
                    self.getData(self.teamID, "Autonomous Med Cones")[length - i] * constants.y) + (
                                 self.getData(self.teamID, "Autonomous Low Cones")[length - i] * constants.z)
            # calculates the points scored from cones in auton
            conesScoredNumA = (self.getData(self.teamID, "Autonomous High Cones")[length - i]) + (
                self.getData(self.teamID, "Autonomous Med Cones")[length - i]) + (
                                  self.getData(self.teamID, "Autonomous Low Cones")[length - i])
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

    def teleopAvg(self):
        global teleTotal
        teleopTotal = 0
        # creates a variable for points scored in teleop for later calculations
        cubesScoredT = 0
        conesScoredT = 0
        # declaring variables for average cones and cubes scored in teleop
        cubePointScoredT = 0
        conePointScoredT = 0
        length = len(self.getData(self.teamID, "Team Number"))

        cubeHighLowT = []
        # declaring array for later use of high/low calculations

        coneHighLowT = []
        # declaring array for later us of high/low calculations

        teleopHighLow = []
        # declaring array for later us of high/low calculations

        for i in range(1, length + 1):
            cubePointT = (self.getData(self.teamID, "Teleop High Cubes")[length - i] * constants.x1) + (
                    self.getData(self.teamID, "Teleop Med Cubes")[length - i] * constants.y1) + (
                                 self.getData(self.teamID, "Teleop Low Cubes")[length - i] * constants.z1)
            # calculates the points scored from cubes in teleop
            cubePointScoredT += cubePointT
            cubePointAvgT = int(round(cubePointScoredT / length, 0))

            cubesScoredNumT = (self.getData(self.teamID, "Teleop High Cubes")[length - i]) + (
                self.getData(self.teamID, "Teleop Med Cubes")[length - i]) + (
                              self.getData(self.teamID, "Teleop Low Cubes")[length - i])
            cubesScoredT += cubesScoredNumT
            cubeAvgT = int(round(cubesScoredT / length, 0))
            # calculates average number of cubes scored by a team in teleop
            cubeHighLowT.append(int(cubePointT))
            cubeHighLowT.sort()
            # appends and sorts a list full of cube score values

            conePointT = (self.getData(self.teamID, "Teleop High Cones")[length - i] * constants.x1) + (
                    self.getData(self.teamID, "Teleop Med Cones")[length - i] * constants.y1) + (
                                 self.getData(self.teamID, "Teleop Low Cones")[length - i] * constants.z1)
            # calculates the points scored from cones in teleop
            conePointScoredT += conePointT
            conePointAvgT = int(round(conePointScoredT / length, 0))

            conesScoredNumT = (self.getData(self.teamID, "Teleop High Cones")[length - i]) + (
                self.getData(self.teamID, "Teleop Med Cones")[length - i]) + (
                              self.getData(self.teamID, "Teleop Low Cones")[length - i])
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

    def endgameAvg(self):
        global endgameTotal
        endgameTotal = 0
        # creates a variable for total points in endgame for calculations
        length = len(self.getData(self.teamID, "Team Number"))

        endgameHighLow = []

        endgameEndPos = (self.getDataStr(self.teamID, "Endgame Ending Position"))

        for i in range(0, length):
            if endgameEndPos[i] == 'None':
                endgameEndPos[i] = 0
            elif endgameEndPos[i] == 'Docked':
                endgameEndPos[i] = 3
            elif endgameEndPos[i] == 'Engaged':
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
        #     endgameBalanceTimeAvg += (getData(self.teamID, "Endgame Time to Balance")[length - i])
        # endgameBalanceTimeAvg = int(round(endgameBalanceTimeAvg/length))
        # calculations for getting the average time to balance during endgame

    def makeDict(self):
        try:
            team1 = {}
            # creates dictionary team1
            team1["Auton Point Low"] = self.autonAvg(self.self.teamID)[0]
            team1["Auton Point Avg"] = self.autonAvg(self.teamID)[1]
            team1["Auton Point High"] = self.autonAvg(self.teamID)[2]
            team1["Teleop Cubes Low"] = self.teleopAvg(self.teamID)[0]
            team1["Teleop Cubes Avg"] = self.teleopAvg(self.teamID)[1]
            team1["Teleop Cubes High"] = self.teleopAvg(self.teamID)[2]
            team1["Teleop Cones Low"] = self.teleopAvg(self.teamID)[3]
            team1["Teleop Cones Avg"] = self.teleopAvg(self.teamID)[4]
            team1["Teleop Cones High"] = self.teleopAvg(self.teamID)[5]
            team1["Endgame Point Low"] = self.endgameAvg(self.teamID)[0]
            team1["Endgame Point Avg"] = self.endgameAvg(self.teamID)[1]
            team1["Endgame Point High"] = self.endgameAvg(self.teamID)[2]
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

            errorUpdate(0, "NO VALID JSON VALUES")
            return team1
        # returns the dictionary team1 to makeDict

    def makeList(self, dataName):
        try:
            tmpData = open(constants.jsonName)
            jsonFile = json.loads(tmpData.read())
            names = jsonFile.keys()
            # turns the json file into a dictionary the python can interact with
            list = []
            # creates a blank array for total (I'm still not exactly sure what total does anymore, I think it gets an array of the values or soemthing)

            maxMatches = 100
            # set the maximum matches

            for i in range(1, maxMatches):
                teamMatchAndNumber = f"{i}_{self}"
                if teamMatchAndNumber in names:
                    valueNames = jsonFile[teamMatchAndNumber].keys()
                    if dataName in valueNames:
                        list.append(jsonFile[teamMatchAndNumber][dataName])
                    else:
                        print(valueNames)
                        errorUpdate(1, 'Possible wrong SCHEMA, try new version')
                        return 0
            # appends the value(s) of a chosen data type into an array for usage later

            return list
            # returns the array total to the function
        except:
            errorUpdate(1, "NO VALID JSON PATH")


    def matches(self):
        matches = len(self.getData("Team Number"))
        return matches

    def printDict(self):
        print(self.makeDict())

    def printMatches(self, ValID):
        print(self.makeList(ValID))
