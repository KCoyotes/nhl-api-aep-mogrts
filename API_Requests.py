import json
import requests

rosterURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster'
teamURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/'

r = requests.get(rosterURL)
t = requests.get(teamURL)

rosterData = r.json()
teamData = t.json()
finalData = {"Example Key" : "Example Value"}
finalData.update(teamData)

from datetime import datetime

now = datetime.now()

timestamp = now.strftime("%B %d, %Y %I:%M:%S %p")
timestampStr = "Data generated on " + timestamp
print(timestampStr)

finalData['DEBUG'] = timestampStr

with open('APIroster.json', 'w', encoding='utf-8') as f:
    json.dump(rosterData, f, ensure_ascii=False, indent=4)

uniqueIDs = []

team = rosterData['teams'][0]['roster']['roster']

for roster in team:
    ID = roster['person']['id']
    uniqueIDs.append(ID)

for player in uniqueIDs:
    statsURL = 'https://statsapi.web.nhl.com/api/v1/people/'
    uniqueURL = statsURL + str(player) + '?hydrate=stats(splits=statsSingleSeason)'
    response = requests.get(uniqueURL)
    playerStats = response.json()
    print("Downloading stats for Player ID: " + str(player))
    print(response)
    finalData['teams'].append(playerStats['people'][0])

print("\nDownload complete. Writing to JSON file...")

with open('API_Stats.json', 'w', encoding='utf-8') as f:
    json.dump(finalData, f, ensure_ascii=False, indent=4)

print("\nLETS GOOOOOOOOOOO\nAPI_Stats.json is ready for import into After Effects!\nStats are up-to-date from NHL.com as of " + timestamp + "\n")
input("Press any key to close this window!")