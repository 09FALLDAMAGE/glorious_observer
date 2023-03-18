from constants import *
import json
import time

start = time.time()

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
    avgs['Autonomous End Of Auton Pos'] = autonPercents
    # injecting the percent arrays

    return [lows, avgs, highs]


print(scrapeJson(67))
end = time.time()
print(end - start)
