import requests
import json
import sys

url = "https://www.thebluealliance.com/api/v3/event/2023mimil/matches/keys"
headers = {
    'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
    'accept': 'application/json'
}

resp = requests.get(url, headers=headers)

MatchNum = 75

tmp = resp.text[1:len(resp.text)-2].replace(" ", "").replace("\"", "").replace(",", "").splitlines()
NameOfMatch = '2023mimil_qm' + str(MatchNum)
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


