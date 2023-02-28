import requests

url = "https://www.thebluealliance.com/api/v3/status"
headers = {
    'X-TBA-Auth-Key': 'TVv0BAIOlUYFeIMLBmOV0BLHqvhYCexcSmnIGLTsOmHdEGoy9fBqK3z0FQfygqZb',
    'accept': 'application/json'
}
resp = requests.get(url, headers=headers)
print(resp.text)
