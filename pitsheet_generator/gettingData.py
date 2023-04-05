import requests
import json
import sys
import sqlite3
import os
#added sql
class gettingTBAData():
    def getData(self, eventName):
        FileName = f"{eventName}.db"
        DistrictKey = eventName
        try:
            url = f"https://www.thebluealliance.com/api/v3/event/{eventName}/matches/keys"
            headers = {
                'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
                'accept': 'application/json'
            }
            resp = requests.get(url, headers=headers)

            WebsiteData = resp.text[1:len(resp.text)-2].replace(" ", "").replace("\"", "").replace(",", "").splitlines()
            print(WebsiteData)
        except:
            return 1

        matchStart = 1 #Starting index for count
        # dataExample = "2023mimil_qm"
        specificmatch = DistrictKey + "_qm" + str(matchStart)
        
        if (FileName in os.listdir()):
            print("removed db file")
            os.remove(FileName)

        con = sqlite3.connect(FileName) #Creates data base if not existing
        cursor = con.cursor()
        cursor.execute("CREATE TABLE matches(matchNum, teamRed1, teamRed2, teamRed3, teamBlue1, teamBlue2, teamBlue3)")

        while (specificmatch in WebsiteData):
            try:
                url = "https://www.thebluealliance.com/api/v3/match/" + specificmatch +"/simple"
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

                sql = f"INSERT INTO matches VALUES (\"qm{matchStart}\", {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
                print(sql)
                cursor.execute(sql)
                matchStart += 1
                specificmatch = DistrictKey + "_qm" + str(matchStart)
            except:
                print(f"Specific match request failed qm{matchStart}")
                matchStart += 1
                specificmatch = DistrictKey + "_qm" + str(matchStart)
            
        matchStart = 1 #Starting index for count
        # dataExample = "2023mimil_qm"
        matchhead = "sf" + str(matchStart) + "m1"
        specificmatch = DistrictKey + "_" + matchhead
        while (specificmatch in WebsiteData):
            try:
                url = "https://www.thebluealliance.com/api/v3/match/" + specificmatch +"/simple"
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

                sql = f"INSERT INTO matches VALUES (\"sf{matchStart}m1\", {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
                print(sql)
                cursor.execute(sql)
                matchStart += 1
                matchhead = "sf" + str(matchStart) + "m1"
                specificmatch = DistrictKey + "_" + matchhead
            except:
                print(f"Specific match request failed {matchhead}")
                matchhead = "sf" + str(matchStart) + "m1"
                specificmatch = DistrictKey + "_" + matchhead
            
        matchStart = 1 #Starting index for count
        # dataExample = "2023mimil_qm"
        matchhead = "sf" + str(matchStart) + "m2"
        specificmatch = DistrictKey + "_" + matchhead
        while (specificmatch in WebsiteData):
            try:
                url = "https://www.thebluealliance.com/api/v3/match/" + specificmatch +"/simple"
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

                sql = f"INSERT INTO matches VALUES (\"sf{matchStart}m2\", {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
                print(sql)
                cursor.execute(sql)
                matchStart += 1
                matchhead = "sf" + str(matchStart) + "m2"
                specificmatch = DistrictKey + "_" + matchhead
            except:
                print(f"Specific match request failed {matchhead}")
                matchhead = "sf" + str(matchStart) + "m2"
                specificmatch = DistrictKey + "_" + matchhead
        
        matchStart = 1 #Starting index for count
        # dataExample = "2023mimil_qm"
        matchhead = "sf" + str(matchStart) + "m3"
        specificmatch = DistrictKey + "_" + matchhead
        while (specificmatch in WebsiteData):
            try:
                url = "https://www.thebluealliance.com/api/v3/match/" + specificmatch +"/simple"
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

                sql = f"INSERT INTO matches VALUES (\"sf{matchStart}m3\", {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
                print(sql)
                cursor.execute(sql)
                matchStart += 1
                matchhead = "sf" + str(matchStart) + "m3"
                specificmatch = DistrictKey + "_" + matchhead
            except:
                print(f"Specific match request failed {matchhead}")
                matchhead = "sf" + str(matchStart) + "m3"
                specificmatch = DistrictKey + "_" + matchhead
        
        matchStart = 1 #Starting index for count
        # dataExample = "2023mimil_qm"
        matchhead = "f1m" + str(matchStart)
        specificmatch = DistrictKey + "_" + matchhead
        while (specificmatch in WebsiteData):
            try:
                url = "https://www.thebluealliance.com/api/v3/match/" + specificmatch +"/simple"
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

                sql = f"INSERT INTO matches VALUES (\"f1m{matchStart}\", {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
                print(sql)
                cursor.execute(sql)
                matchStart += 1
                matchhead = "f1m" + str(matchStart)
                specificmatch = DistrictKey + "_" + matchhead
            except:
                print(f"Specific match request failed {matchhead}")
                matchhead = "f1m" + str(matchStart)
                specificmatch = DistrictKey + "_" + matchhead

        print("done")
        print("Remember, whatever you named the file will need to be inputed into the pitsheet generator, it is whatever you named it then .db")

        con.commit()
        return FileName
