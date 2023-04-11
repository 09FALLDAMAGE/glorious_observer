import constants
from constants import *
import json

rawFile = open(constants.jsonName)
jsonData = json.loads(rawFile.read())
matches = jsonData.keys()
rawFile.close()

blacklist = {"Autonomous Starting Position": None, "Teleop Preferred Pickup Position": None}
# values we don't care about

chargingKeys = {"Autonomous End Of Auton Pos": None, "Endgame Ending Position": None}


# climbing/balancing names


def scrapeJson(teamNumber):
    maxMatches = 76
    matchesElapsed = 0
    autonPieceAvg = 0
    telePieceAvg = 0
    autonPiecesLow = 999999999
    autonPiecesHigh = 0
    telePiecesLow = 999999999
    telePiecesHigh = 0
    autonAttempts = 0
    endgameAttempts = 0
    matchNums = []

    lows = {}
    highs = {}
    teamMD = {}
    avgs = {}
    autonPercents = [0, 0, 0]
    endgamePercents = [0, 0, 0, 0]
    autonPieces = []
    telePieces = []
    # all the dictionarys and arrays that data is put in

    for i in range(1, maxMatches):
        teamMatch = f"{i}_{teamNumber}"

        # creating a key that interfaces with the first level of the json
        if teamMatch in matches:
            jsonData[teamMatch].pop('Teleop Scouting Shift', None)
            jsonData[teamMatch].pop('Teleop Cool Robot', None)
            jsonData[teamMatch].pop('Team Number', None)
            jsonData[teamMatch].pop('Notes', None)
            jsonData[teamMatch].pop('Endgame Time Playing Defense', None)
            # clean any 100% unnessesary data to improve preformance and simplicity

            teamMD[matchesElapsed] = jsonData[teamMatch]
            # all json numbers import as strings, this tries to make everything a number.
            # If it can't, it passes the string through

            matchNums.append(i)
            matchesElapsed += 1
            # this creates an array and int that let us find what matches a robot was in,
            # and how many matches we have data on

    for i in range(matchesElapsed):
        autonPieces.append(int(teamMD[i]["Autonomous High Cones"]) + int(teamMD[i]["Autonomous High Cubes"]) + int(
            teamMD[i]["Autonomous Low Cones"]) + int(teamMD[i]["Autonomous Low Cubes"]) + int(
            teamMD[i]["Autonomous Med Cones"]) + int(teamMD[i]["Autonomous Med Cubes"]))
        autonPieceAvg += autonPieces[i]

        if autonPieces[i] < autonPiecesLow:
            autonPiecesLow = autonPieces[i]

        if autonPieces[i] > autonPiecesHigh:
            autonPiecesHigh = autonPieces[i]

    autonPieceAvg /= matchesElapsed


    for i in range(matchesElapsed):
        telePieces.append(int(teamMD[i]["Teleop High Cones"]) + int(teamMD[i]["Teleop High Cubes"]) + int(
            teamMD[i]["Teleop Low Cones"]) + int(teamMD[i]["Teleop Low Cubes"]) + int(
            teamMD[i]["Teleop Med Cones"]) + int(teamMD[i]["Teleop Med Cubes"]))
        telePieceAvg += telePieces[i]

        if telePieces[i] < telePiecesLow:
            telePiecesLow = telePieces[i]

        if telePieces[i] > telePiecesHigh:
            telePiecesHigh = telePieces[i]

    telePieceAvg /= matchesElapsed

    for key in teamMD[0].keys():
        # this looks through all the keys in the first match the team played as a base
        if key not in blacklist:
            lows[key] = 9999999999999999999999999999999999
            # absurd number to ensure no weird data can crash it
            highs[key] = 0
            # nothing can be lower than 0
            avgs[key] = 0
            # define the value for the key, so we can directly do math
            for i in range(matchesElapsed):
                try:
                    teamMD[i][key] = int(teamMD[i][key])
                except:
                    lows.pop(key, None)
                    highs.pop(key, None)

                if type(teamMD[i][key]) == int:
                    # this runs the function only for numbers
                    if teamMD[i][key] < lows[key]:
                        lows[key] = teamMD[i][key]

                    if teamMD[i][key] > highs[key]:
                        highs[key] = teamMD[i][key]

                    # this gets the low and high values more efficiently than max() or min()

                if teamMD[i][key] == 'true':
                    teamMD[i][key] = 1
                elif teamMD[i][key] == 'false':
                    teamMD[i][key] = 0
                # this converts boolean values to a 1 or a 0, so we can do math

                if key == 'Endgame Ending Position':
                    # calculating climbing percentages for endgame

                    if teamMD[i]["Endgame Charge Attempt"] == 1:
                        endgameAttempts += 1
                        if teamMD[i][key] == 'Engaged':
                            endgamePercents[0] += 1
                        elif teamMD[i][key] == 'Docked':
                            endgamePercents[1] += 1
                        elif teamMD[i][key] == 'Nothing':
                            endgamePercents[2] += 1
                    else:
                        if teamMD[i][key] == 'Parked':
                            endgamePercents[3] += 1
                        elif teamMD[i][key] == 'Nothing':
                            endgamePercents[2] += 1

                if key == 'Autonomous End Of Auton Pos':
                    # calculating climbing percentages for auton

                    if teamMD[i]["Autonomous Charge Attempt"] == 1:
                        autonAttempts += 1

                        if teamMD[i][key] == 'Engaged':
                            autonPercents[0] += 1
                        elif teamMD[i][key] == 'Docked':
                            autonPercents[1] += 1
                        elif teamMD[i][key] == 'Nothing':
                            autonPercents[2] += 1
                    else:
                        autonPercents[2] += 1

                if type(teamMD[i][key]) == int:
                    # this runs the function only for numbers
                    avgs[key] += teamMD[i][key]

            avgs[key] = avgs[key] / matchesElapsed
            # this divides out the averages for each category

    for i in range(3):
        try:
            endgamePercents[i] = (endgamePercents[i] / endgameAttempts) * 100
        except:
            endgamePercents[i] = 0

        try:
            autonPercents[i] = (autonPercents[i] / autonAttempts) * 100
        except:
            autonPercents[i] = 0


    endgamePercents[3] = endgamePercents[3] / matchesElapsed

    # this calculates the percent of the time that a robot climbs

    avgs['Endgame Ending Position'] = endgamePercents
    avgs['Auton Piece'] = autonPieceAvg
    avgs['Teleop Piece'] = telePieceAvg
    avgs['Autonomous End Of Auton Pos'] = autonPercents
    avgs['Auton Attempts'] = autonAttempts
    avgs['Endgame Attempts'] = endgameAttempts
    # injecting the percent arrays
    lows['Autonomous Cross Line'] = 0
    lows['Auton Piece'] = autonPiecesLow
    highs['Auton Piece'] = autonPiecesHigh
    lows['Teleop Piece'] = autonPiecesLow
    highs['Teleop Piece'] = autonPiecesHigh
    highs['Autonomous Cross Line'] = 0

    return [lows, avgs, highs]


def scrapePoints(teamNumber):
    dat = scrapeJson(teamNumber)
    for i in range(3):
        dat[i]['Autonomous High Cubes'] *= constants.h
        dat[i]['Autonomous Med Cubes'] *= constants.m
        dat[i]['Autonomous Low Cubes'] *= constants.l

        dat[i]['Autonomous High Cones'] *= constants.h
        dat[i]['Autonomous Med Cones'] *= constants.m
        dat[i]['Autonomous Low Cones'] *= constants.l

        dat[i]['Teleop High Cubes'] *= constants.h1
        dat[i]['Teleop Med Cubes'] *= constants.m1
        dat[i]['Teleop Low Cubes'] *= constants.l1

        dat[i]['Teleop High Cones'] *= constants.h1
        dat[i]['Teleop Med Cones'] *= constants.m1
        dat[i]['Teleop Low Cones'] *= constants.l1

        dat[i]['Teleop Point'] = dat[i]['Teleop High Cubes'] + dat[i]['Teleop Med Cubes'] + \
                                 dat[i]['Teleop Low Cubes'] + dat[i]['Teleop High Cones'] + \
                                 dat[i]['Teleop Med Cones'] + dat[i]['Teleop Low Cones']

        dat[i]['Auton Point'] = (dat[i]['Autonomous Cross Line'] * constants.c) + dat[i]['Autonomous High Cubes'] + \
                                dat[i]['Autonomous Med Cubes'] + dat[i]['Autonomous Low Cubes'] + dat[i][
                                    'Autonomous High Cones'] + \
                                dat[i]['Autonomous Med Cones'] + dat[i]['Autonomous Low Cones']

    dat[0]['Endgame Point'] = 0
    dat[1]['Endgame Point'] = ((dat[1]['Endgame Ending Position'][0] / 100) * constants.e1) + (
            (dat[1]['Endgame Ending Position'][1] / 100) * constants.d1) + (
            (dat[1]['Endgame Ending Position'][1] / 100) * constants.c1)
    dat[2]['Endgame Point'] = 10

    # inefficent low endgame calcs

    if (dat[1]['Endgame Ending Position'][0] / 100) != 0:
        dat[2]['Endgame Point'] = constants.e1
    elif (dat[1]['Endgame Ending Position'][1] / 100) != 0:
        dat[2]['Endgame Point'] = constants.d1
    elif dat[1]['Endgame Ending Position'][3] != 0:
        dat[2]['Endgame Point'] = constants.c1
    else:
        dat[2]['Endgame Point'] = 0


    if (dat[1]['Endgame Ending Position'][2] / 100) != 0:
        dat[0]['Endgame Point'] = 0
    elif (dat[1]['Endgame Ending Position'][3] / 100) != 0:
        dat[0]['Endgame Point'] = constants.c1
    elif dat[1]['Endgame Ending Position'][1] != 0:
        dat[0]['Endgame Point'] = constants.d1
    elif dat[1]['Endgame Ending Position'][0] != 0:
        dat[0]['Endgame Point'] = constants.e1
    else:
        dat[0]['Endgame Point'] = 0

    return dat


def makeDict(teamNumber):
    dat = scrapePoints(teamNumber)

    try:
        team1 = {}
        # creates dictionary team1

        team1["Auton Point Low"] = dat[0]['Auton Point']
        team1["Auton Point Avg"] = dat[1]['Auton Point']
        team1["Auton Point High"] = dat[2]['Auton Point']
        team1["Auton Piece Low"] = dat[0]['Auton Piece']
        team1["Auton Piece Avg"] = dat[1]['Auton Piece']
        team1["Auton Piece High"] = dat[2]['Auton Piece']

        team1["Teleop Point Low"] = dat[0]['Teleop Point']
        team1["Teleop Point Avg"] = dat[1]['Teleop Point']
        team1["Teleop Point High"] = dat[2]['Teleop Point']
        team1["Teleop Piece Low"] = dat[0]['Teleop Piece']
        team1["Teleop Piece Avg"] = dat[1]['Teleop Piece']
        team1["Teleop Piece High"] = dat[2]['Teleop Piece']

        team1["Auton Attempts"] = dat[1]['Auton Attempts']
        team1["Endgame Attempts"] = dat[1]['Endgame Attempts']

        team1["Auton None Percent"] = round(dat[1]['Autonomous End Of Auton Pos'][2])
        team1["Auton Docked Percent"] = round(dat[1]['Autonomous End Of Auton Pos'][1])
        team1["Auton Engaged Percent"] = round(dat[1]['Autonomous End Of Auton Pos'][0])

        team1["Auton Cubes Low"] = dat[0]['Autonomous Low Cubes'] + dat[0]['Autonomous Med Cubes'] + dat[0][
            'Autonomous High Cubes']
        team1["Auton Cubes Avg"] = dat[1]['Autonomous Low Cubes'] + dat[1]['Autonomous Med Cubes'] + dat[1][
            'Autonomous High Cubes']
        team1["Auton Cubes High"] = dat[2]['Autonomous Low Cubes'] + dat[2]['Autonomous Med Cubes'] + dat[2][
            'Autonomous High Cubes']
        team1["Auton Cones Low"] = dat[0]['Autonomous Low Cones'] + dat[0]['Autonomous Med Cones'] + dat[0][
            'Autonomous High Cones']
        team1["Auton Cones Avg"] = dat[1]['Autonomous Low Cones'] + dat[1]['Autonomous Med Cones'] + dat[1][
            'Autonomous High Cones']
        team1["Auton Cones High"] = dat[2]['Autonomous Low Cones'] + dat[2]['Autonomous Med Cones'] + dat[2][
            'Autonomous High Cones']
        team1["Teleop Cubes Low"] = dat[0]['Teleop Low Cubes'] + dat[0]['Teleop Med Cubes'] + dat[0][
            'Teleop High Cubes']
        team1["Teleop Cubes Avg"] = dat[1]['Teleop Low Cubes'] + dat[1]['Teleop Med Cubes'] + dat[1][
            'Teleop High Cubes']
        team1["Teleop Cubes High"] = dat[2]['Teleop Low Cubes'] + dat[2]['Teleop Med Cubes'] + dat[2][
            'Teleop High Cubes']
        team1["Teleop Cones Low"] = dat[0]['Teleop Low Cones'] + dat[0]['Teleop Med Cones'] + dat[0][
            'Teleop High Cones']
        team1["Teleop Cones Avg"] = dat[1]['Teleop Low Cones'] + dat[1]['Teleop Med Cones'] + dat[1][
            'Teleop High Cones']
        team1["Teleop Cones High"] = dat[2]['Teleop Low Cones'] + dat[2]['Teleop Med Cones'] + dat[2][
            'Teleop High Cones']
        team1["Endgame None Percent"] = round(dat[1]['Endgame Ending Position'][2])
        team1["Endgame Docked Percent"] = round(dat[1]['Endgame Ending Position'][1])
        team1["Endgame Engaged Percent"] = round(dat[1]['Endgame Ending Position'][0])
        team1["Endgame Point Low"] = dat[0]['Endgame Point']
        team1["Endgame Point Avg"] = dat[1]['Endgame Point']
        team1["Endgame Point High"] = dat[2]['Endgame Point']

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
        team1["Endgame None Percent"] = "null"
        team1["Endgame Docked Percent"] = "null"
        team1["Endgame Engaged Percent"] = "null"
        # populates the dictionary team1

        return team1
    # returns the dictionary team1 to makeDict
