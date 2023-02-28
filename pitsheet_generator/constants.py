class constants:
    defaultJson = '2023test2.json'

    jsonName = defaultJson

    x = 6
    # high cone/cube point value auton

    y = 4
    # medium cube/cone point value auton

    z = 3
    # low cone/cube point value auton

    x1 = 5
    # high cone/cube point value teleop

    y1 = 3
    # medium cube/cone point value teleop

    z1 = 2
    # low cone/cube point value teleop

    barMult = 7
    # bar multipliers

    prefixes = ['Auton Cones ', 'Auton Cones ', 'Teleop Cubes ', 'Teleop Cubes ', 'Endgame Point ', 'Auton Point ']
    # dictionary prefixes used in teamcard

    suffixes = ['Low', 'Avg', 'High']

    percentPrefix = ['Auton ', 'Endgame ']

    percentSuff = ['None ', 'Docked ', 'Engaged ']
    # dictionary suffixes used in teamcard

    version = '1.5'

    def setJsonName(self, jsoner):
        jsonName = jsoner

