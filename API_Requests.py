import json
import requests

url = 'https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster'

r = requests.get(url)

data = r.json()

with open('APIroster.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

uniqueIDs = []

team = data['teams'][0]['roster']['roster']

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
    data['teams'][0]['roster']['roster'][0]['person'].append(playerStats['people'])

with open('API_Stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)