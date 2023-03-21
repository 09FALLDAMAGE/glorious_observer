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
    matchNums = []

    lows = {}
    highs = {}
    teamMD = {}
    avgs = {}
    autonPercents = [0, 0, 0]
    endgamePercents = [0, 0, 0]
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

                if key == 'Endgame Ending Position':
                    # calculating climbing percentages for endgame
                    if teamMD[i][key] == 'Engaged':
                        endgamePercents[0] += 1
                    elif teamMD[i][key] == 'Docked':
                        endgamePercents[1] += 1
                    elif teamMD[i][key] == 'Nothing':
                        endgamePercents[2] += 1

                elif key == 'Autonomous End Of Auton Pos':
                    # calculating climbing percentages for auton
                    if teamMD[i][key] == 'Engaged':
                        autonPercents[0] += 1
                    elif teamMD[i][key] == 'Docked':
                        autonPercents[1] += 1
                    elif teamMD[i][key] == 'Nothing':
                        autonPercents[2] += 1

                if teamMD[i][key] == 'true':
                    teamMD[i][key] = 1
                elif teamMD[i][key] == 'false':
                    teamMD[i][key] = 0
                # this converts boolean values to a 1 or a 0, so we can do math

                if type(teamMD[i][key]) == int:
                    # this runs the function only for numbers
                    avgs[key] += teamMD[i][key]

            avgs[key] = avgs[key] / matchesElapsed
            # this divides out the averages for each category

    for i in range(3):
        endgamePercents[i] = (endgamePercents[i] / matchesElapsed) * 100
        autonPercents[i] = (autonPercents[i] / matchesElapsed) * 100

        # this calculates the percent of the time that a robot climbs

    avgs['Endgame Ending Position'] = endgamePercents
    print(avgs['Endgame Ending Position'])
    avgs['Autonomous End Of Auton Pos'] = autonPercents
    print(avgs['Autonomous End Of Auton Pos'])
    # injecting the percent arrays
    lows['Autonomous Cross Line'] = 0
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

        dat[i]['Auton Point'] = (dat[i]['Autonomous Cross Line'] * constants.m) + dat[i]['Autonomous High Cubes'] + \
            dat[i]['Autonomous Med Cubes'] + dat[i]['Autonomous Low Cubes'] + dat[i]['Autonomous High Cones'] + \
            dat[i]['Autonomous Med Cones'] + dat[i]['Autonomous Low Cones']

        dat[i]['Endgame Point'] = (dat[1]['Endgame Ending Position'][0] * constants.e1) + (dat[1]['Endgame Ending Position'][1] * constants.d1)

    return dat


def makeDict(teamNumber):
    dat = scrapePoints(teamNumber)

    try:
        team1 = {}
        # creates dictionary team1

        team1["Auton Point Low"] = dat[0]['Auton Point']
        team1["Auton Point Avg"] = dat[1]['Auton Point']
        team1["Auton Point High"] = dat[2]['Auton Point']
        print('checkpoint 1.2')
        team1["Auton None Percent"] = dat[1]['Autonomous End Of Auton Pos'][2]
        print('checkpoint 1.5')
        team1["Auton Docked Percent"] = dat[1]['Autonomous End Of Auton Pos'][1]
        team1["Auton Engaged Percent"] = dat[1]['Autonomous End Of Auton Pos'][0]
        print('checkpoint 2')
        team1["Auton Cubes Low"] = dat[0]['Autonomous Low Cubes'] + dat[0]['Autonomous Med Cubes'] + dat[0]['Autonomous High Cubes']
        team1["Auton Cubes Avg"] = dat[1]['Autonomous Low Cubes'] + dat[1]['Autonomous Med Cubes'] + dat[1]['Autonomous High Cubes']
        team1["Auton Cubes High"] = dat[2]['Autonomous Low Cubes'] + dat[2]['Autonomous Med Cubes'] + dat[2]['Autonomous High Cubes']
        team1["Auton Cones Low"] = dat[0]['Autonomous Low Cones'] + dat[0]['Autonomous Med Cones'] + dat[0]['Autonomous High Cones']
        team1["Auton Cones Avg"] = dat[1]['Autonomous Low Cones'] + dat[1]['Autonomous Med Cones'] + dat[1]['Autonomous High Cones']
        team1["Auton Cones High"] = dat[2]['Autonomous Low Cones'] + dat[2]['Autonomous Med Cones'] + dat[2]['Autonomous High Cones']
        team1["Teleop Cubes Low"] = dat[0]['Teleop Low Cubes'] + dat[0]['Teleop Med Cubes'] + dat[0]['Teleop High Cubes']
        team1["Teleop Cubes Avg"] = dat[1]['Teleop Low Cubes'] + dat[1]['Teleop Med Cubes'] + dat[1]['Teleop High Cubes']
        team1["Teleop Cubes High"] = dat[2]['Teleop Low Cubes'] + dat[2]['Teleop Med Cubes'] + dat[2]['Teleop High Cubes']
        team1["Teleop Cones Low"] = dat[0]['Teleop Low Cones'] + dat[0]['Teleop Med Cones'] + dat[0]['Teleop High Cones']
        team1["Teleop Cones Avg"] = dat[1]['Teleop Low Cones'] + dat[1]['Teleop Med Cones'] + dat[1]['Teleop High Cones']
        team1["Teleop Cones High"] = dat[2]['Teleop Low Cones'] + dat[2]['Teleop Med Cones'] + dat[2]['Teleop High Cones']
        team1["Endgame None Percent"] = dat[1]['Endgame Ending Position'][2]
        team1["Endgame Docked Percent"] = dat[1]['Endgame Ending Position'][1]
        team1["Endgame Engaged Percent"] = dat[1]['Endgame Ending Position'][0]
        team1["Endgame Point Low"] = "null"
        team1["Endgame Point Avg"] = "null"
        team1["Endgame Point High"] = "null"


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
