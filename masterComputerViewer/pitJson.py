import json
from constants import *


def getPitData(teamNumber):
    tmpData = open(constants.pitName)
    jsonFile = json.loads(tmpData.read())
    names = jsonFile.keys()
    total = jsonFile[teamNumber]
    return total
