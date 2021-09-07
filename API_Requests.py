import json
import requests
import time
import zipfile

print("   ____________  ______  _________________")
print("  / ____/ __ \ \/ / __ \/_  __/ ____/ ___/")
print(" / /   / / / /\  / / / / / / / __/  \__ \ ")
print("/ /___/ /_/ / / / /_/ / / / / /___ ___/ / ")
print("\____/\____/ /_/\____/ /_/ /_____//____/  ")
print("                                          ")
print("nhl-api-aep-mogrts | v0.2 Build 20")
print("Scrape info from the NHL's Stats API\n")
print("Created by Kevin Thompson")
print("")
input("\nPress any key to start downloading...")

from datetime import datetime

now = datetime.now()

timestamp = now.strftime("%B %d, %Y %I:%M:%S %p")
timestampStr = "Data generated on " + timestamp

rosterURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster'
teamURL = 'https://statsapi.web.nhl.com/api/v1/teams/53/'

r = requests.get(rosterURL)
t = requests.get(teamURL)

rosterData = r.json()
teamData = t.json()
finalData = {"TIMESTAMP" : timestampStr}
finalData.update(teamData)

print("\n" + timestampStr + "\n")

finalData['DEBUG'] = timestampStr

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
    print("Downloading stats for Player ID: " + str(player) + "...")
    finalData['teams'].append(playerStats['people'][0])

print("\nDownload complete. Writing to JSON file...")

with open('MOGRTs\\(Footage)\\API_Stats.json', 'w', encoding='utf-8') as f:
    json.dump(finalData, f, ensure_ascii=False, indent=4)

print("\nLETS GOOOOOOOOOOO\nAPI_Stats.json is ready for import into After Effects!\nStats are up-to-date from NHL.com as of " + timestamp + "\n")

time.sleep(1)

print("Packaging .aegraphic file...")

with zipfile.ZipFile('MOGRTs\\project.aegraphic', 'w', compression=zipfile.ZIP_DEFLATED) as aegraphic:
    aegraphic.write('MOGRTs\\Main.aep', 'Main.aep')
    aegraphic.write('MOGRTs\\MainReport.txt', 'MainReport.txt')
    aegraphic.write('MOGRTs\\(Footage)\\API_Stats.json', '(Footage)\\API_Stats.json')
    aegraphic.write('MOGRTs\\(Footage)\\Neon Kachina Purple.png', '(Footage)\\Neon Kachina Purple.png')
print("Done!\n")


print("Writing definitions.json...")

shortTimestamp = now.strftime("%x, %X")

with open('MOGRTs\\definition.json') as d:
    definition = json.load(d)
definition['capsuleNameLocalized']['strDB'][0]['str'] = 'API Testing ' + shortTimestamp

definition['clientControls'][3]['value']['strDB'][0]['str'] = timestamp

with open('MOGRTs\\definition.json', 'w', encoding='utf-8') as x:
    json.dump(definition, x, ensure_ascii=False)

print("Done!\n")


print("Packaging .mogrt file...")

with zipfile.ZipFile('MOGRTs\\Player L3 API.mogrt', 'w', compression=zipfile.ZIP_DEFLATED) as mogrt:
        mogrt.write('MOGRTs\\definition.json', 'definition.json')
        mogrt.write('MOGRTs\\thumb.png', 'thumb.png')
        mogrt.write('MOGRTs\\project.aegraphic', 'project.aegraphic')
print("Done!\n\n")
print("MOGRT exported successfully! Check the Essential Graphics panel in Premiere.\n\nMake sure you've added the 'MOGRTs' folder to your\nwatched folders in the Essential Graphics panel.\n")

input("Press any key to close this window!")