import sqlite3

con = sqlite3.connect("matches.db")
cursor = con.cursor()
wantedMatchNum = 30

res = cursor.execute(f"SELECT * FROM matches WHERE matchNum = {wantedMatchNum}")
print(res.fetchall()[0][1:])