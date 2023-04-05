from errorHandeler import errorUpdate
from constants import constants
from pitSheet import generatePitSheet
import os
import requests as rq
import json
import sys
import sqlite3


class requests:
    def __init__(self):
        self.isValid = False

        self.dir_list = os.listdir()
        self.overide = True

    def refresh(self, eventCode):
        # event code example: 2023mimil
        return None

    def start(self, match, jsonPath):
        self.checkValid(jsonPath)

        if self.isValid:
            con = sqlite3.connect("matches.db")
            cursor = con.cursor()
            res = cursor.execute(f"SELECT * FROM matches WHERE matchNum = {match}")
            teams = res.fetchall()[0][1:]
            red = [teams[0], teams[1], teams[2]]
            blue = [teams[3], teams[4], teams[5]]
            
            generatePitSheet(match, blue, red).generateSheet()

    def checkValid(self, path):
        for i in range(len(self.dir_list) - 1):
            if self.dir_list[i] == path:
                self.isValid = True
        if self.isValid:
            return True
        else:
            errorUpdate(1, 'not a valid json name')
            return False

