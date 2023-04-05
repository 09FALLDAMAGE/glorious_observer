import requests
import json
import sys
import sqlite3

FileName = input("Enter database name here (.db): ")
DistrictKey = input("Enter districtkey here (examples: 2023mimil_qm, 2023mimil_f1m, etc.): ")

url = "https://www.thebluealliance.com/api/v3/event/2023mimil/matches/keys"
headers = {
    'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
    'accept': 'application/json'
}
resp = requests.get(url, headers=headers)

WebsiteData = resp.text[1:len(resp.text)-2].replace(" ", "").replace("\"", "").replace(",", "").splitlines()
print(WebsiteData)

matchStart = 1 #Starting index for count
# dataExample = "2023mimil_qm"
specificmatch = DistrictKey + str(matchStart)

con = sqlite3.connect(f"{FileName}.db") #Creates data base if not existing
cursor = con.cursor()
cursor.execute("CREATE TABLE matches(matchNum, teamRed1, teamRed2, teamRed3, teamBlue1, teamBlue2, teamBlue3)")

while (specificmatch in WebsiteData):
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


    sql = f"INSERT INTO matches VALUES ({matchStart}, {red[0]}, {red[1]}, {red[2]}, {blue[0]}, {blue[1]}, {blue[2]})"
    print(sql)
    cursor.execute(sql)
    matchStart += 1
    specificmatch = DistrictKey + str(matchStart)

print("done")
print("Remember, whatever you named the file will need to be inputed into the pitsheet generator, it is whatever you named it then .db")

con.commit()
