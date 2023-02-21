from pitSheet import *
from errorHandeler import *
import os


class requests:
    def __init__(self):
        self.isValid = False

        self.dir_list = os.listdir()

    def start(self, match, jsonPath):
        self.checkValid(jsonPath)

        if self.isValid:
            print(self.dir_list)
            generatePitSheet(match, [503, 503, 503], [503, 503, 503]).generateSheet()

    def checkValid(self, path):
        for i in range(len(self.dir_list) - 1):
            if self.dir_list[i] == path:
                self.isValid = True

        if self.isValid:
            return True
        else:
            errorHandeler.errorUpdate(1, 'not a valid json name')
            return False
