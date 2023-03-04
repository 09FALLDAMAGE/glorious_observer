from errorHandeler import errorUpdate
from constants import constants
from pitSheet import generatePitSheet
import os
import requests
import json
import sys


class requests:
    def __init__(self):
        self.isValid = False

        self.dir_list = os.listdir()

    def start(self, match, jsonPath):
        self.checkValid(jsonPath)

        if self.isValid:
            # print(self.dir_list)
            constants().setJsonName(jsonPath)

            url = "https://www.thebluealliance.com/api/v3/event/2023mimil/matches/keys"
            headers = {
                'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
                'accept': 'application/json'
            }

            resp = requests.get(url, headers=headers)


            tmp = resp.text[1:len(resp.text)-2].replace(" ", "").replace("\"", "").replace(",", "").splitlines()
            NameOfMatch = '2023mimil_qm' + str(match)
            if (NameOfMatch in tmp):
                print(NameOfMatch)
                url = "https://www.thebluealliance.com/api/v3/match/" + NameOfMatch +"/simple"
                headers = {
                    'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
                    'accept': 'application/json'
                }
                resp = requests.get(url, headers=headers)
                data = json.loads(resp.text)
                redRaw = data["alliances"]["red"]["team_keys"]
                blueRaw = data["alliances"]["blue"]["team_keys"]
                red = [int(el.replace("frc", "")) for el in redRaw]
                blue = [int(el.replace("frc", "")) for el in blueRaw]
                print(red)
                print(blue)
            else:
                sys.exit(1)
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

