from errorHandeler import errorUpdate
from constants import constants
from pitSheet import generatePitSheet
import os


class requests:
    def __init__(self):
        self.isValid = False

        self.dir_list = os.listdir()

    def start(self, match, jsonPath):
        self.checkValid(jsonPath)

        if self.isValid:
            # print(self.dir_list)
            constants().setJsonName(jsonPath)
            generatePitSheet(match, [3414, 3707, 7224], [3538, 67, 9204]).generateSheet()

    def checkValid(self, path):
        for i in range(len(self.dir_list) - 1):
            if self.dir_list[i] == path:
                self.isValid = True
        if self.isValid:
            return True
        else:
            errorUpdate(1, 'not a valid json name')
            return False

