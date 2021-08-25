import json
import requests

rosterURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster'
teamURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/'

r = requests.get(rosterURL)
t = requests.get(teamURL)

rosterData = r.json()
teamData = t.json()

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
    print(uniqueURL)
    response = requests.get(uniqueURL)
    print(response)
    playerStats = response.json()
    print(player)
    teamData['teams'].append(playerStats['people'])

with open('API_Stats.json', 'w', encoding='utf-8') as f:
    json.dump(teamData, f, ensure_ascii=False, indent=4)