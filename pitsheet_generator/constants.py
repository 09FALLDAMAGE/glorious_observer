class constants:
    defaultJson = 'attempt.json'

    defaultEvent = '2023mimil'

    jsonName = defaultJson

    eventName = defaultEvent

    h = 6
    # high cone/cube point value auton
    m = 4
    # medium cube/cone point value auton
    l = 3
    # low cone/cube point value auton

    h1 = 5
    # high cone/cube point value teleop
    m1 = 3
    # medium cube/cone point value teleop
    l1 = 2
    # low cone/cube point value teleop

    c = 3
    # cross line in auto
    c1 = 2
    # cross line in endgame

    d = 8
    # dock in auton
    d1 = 6
    # dock in endgame

    e = 12
    # engage in auton
    e1 = 10
    # engage in endgame


    barMult = 6
    # bar multipliers

    prefixes = ['Auton Point ', 'Auton Piece ', 'Teleop Point ', 'Teleop Piece ', 'Endgame Point ']
    # dictionary prefixes used in teamcard
    totalPrefixes = ['Auton Point ', 'Teleop Point ', 'Endgame Point ']

    suffixes = ['Low', 'Avg', 'High']

    percentPrefix = ['Auton ', 'Endgame ']

    percentSuff = ['Attempts', 'Docked Percent', 'Engaged Percent']
    # dictionary suffixes used in teamcard

    version = '3.0'

    def setJsonName(self, jsoner):
        jsonName = jsoner

    def setEventCode(self, eventer):
        eventName = eventer

