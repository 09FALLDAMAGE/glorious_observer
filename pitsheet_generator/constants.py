class constants:
    defaultJson = '2023mimil.json'

    jsonName = defaultJson

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

    prefixes = ['Auton Cones ', 'Auton Cubes ', 'Teleop Cones ', 'Teleop Cubes ', 'Endgame Point ', 'Auton Point ']
    # dictionary prefixes used in teamcard
    totalPrefixes = ['Auton Point ', 'Teleop Cones ', 'Teleop Cubes ', 'Endgame Point ', 'Auton Point ']

    suffixes = ['Low', 'Avg', 'High']

    percentPrefix = ['Auton ', 'Endgame ']

    percentSuff = ['None ', 'Docked ', 'Engaged ']
    # dictionary suffixes used in teamcard

    version = '1.8'

    def setJsonName(self, jsoner):
        jsonName = jsoner

