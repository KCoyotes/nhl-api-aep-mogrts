import os
import json
from re import search
import requests
import time
import zipfile
from tqdm import tqdm
from alive_progress import alive_bar

print("   ____________  ______  _________________")
print("  / ____/ __ \ \/ / __ \/_  __/ ____/ ___/")
print(" / /   / / / /\  / / / / / / / __/  \__ \ ")
print("/ /___/ /_/ / / / /_/ / / / / /___ ___/ / ")
print("\____/\____/ /_/\____/ /_/ /_____//____/  ")
print("                                          ")
print("nhl-api-renamer | v0.1 Build 1")
print("Rename Headshots using NHL's Stats API\n")
print("Created by Kevin Thompson")
print("")

from datetime import datetime

now = datetime.now()

timestamp = now.strftime("%B %d, %Y %I:%M:%S %p")
timestampStr = "Data generated on " + timestamp

teamsURL = 'https://statsapi.web.nhl.com/api/v1/teams'
requestTeams = requests.get(teamsURL)
teams = requestTeams.json()

teamSelect = input("Enter the Tricode for your team: ")

"""
def search_tricode (abbreviation):
    for keyval in teams['teams']:
        if abbreviation.lower() == keyval['abbreviation'].lower():
            return keyval['id']

if (search_tricode(teamSelect) != None):
    print("The ID for the team you selected is ", search_tricode(teamSelect))
else:
    print("Team not found.")
"""

selectedTeam = list(filter(lambda x:x["abbreviation"]==teamSelect,teams['teams']))
print(selectedTeam[0]['id'], selectedTeam[0]['name'])


rosterURL = 'https://statsapi.web.nhl.com/api/v1/teams/' + str(selectedTeam[0]['id']) + '/?expand=team.roster'
teamURL = 'https://statsapi.web.nhl.com/api/v1/teams/' + str(selectedTeam[0]['id']) + '/'


r = requests.get(rosterURL)
t = requests.get(teamURL)

rosterData = r.json()
teamData = t.json()
finalData = {"TIMESTAMP" : timestampStr}
finalData.update(teamData)

copyright=finalData['copyright'].split(". ", 2)
print("\n\n" + copyright[0] + ".\n" + copyright[1] + ".\n" + copyright[2] + "\n")
time.sleep(1)
print(timestampStr + "\n")
time.sleep(1)

finalData['DEBUG'] = timestampStr

uniqueIDs = []

team = rosterData['teams'][0]['roster']['roster']

for roster in team:
    ID = roster['person']['id']
    uniqueIDs.append(ID)

with alive_bar(len(uniqueIDs), length=30, bar='smooth', enrich_print=False) as bar:
    for player in uniqueIDs:
        statsURL = 'https://statsapi.web.nhl.com/api/v1/people/'
        uniqueURL = statsURL + str(player) + '?hydrate=stats(splits=statsSingleSeason)'
        response = requests.get(uniqueURL)
        playerStats = response.json()
        print("Renaming NHL Headshot " + str(player) + " to " + playerStats['people'][0]['lastName'] + "_" + playerStats['people'][0]['firstName'])
        file_path = 'C:\\Renamer3\\'
        if os.path.exists(file_path + str(player) + '.jpg'):
            os.rename(file_path + str(player) + '.jpg', file_path + playerStats['people'][0]['lastName'] + "_" + playerStats['people'][0]['firstName'] + '.jpg')
        else:
            print('Skipped')
        bar()

print("\nRenaming Complete!")
"""
with alive_bar(len(uniqueIDs), length=30, bar='smooth', enrich_print=False) as bar:
    for player in uniqueIDs:
        statsURL = 'https://statsapi.web.nhl.com/api/v1/people/'
        uniqueURL = statsURL + str(player) + '?hydrate=stats(splits=statsSingleSeason)'
        response = requests.get(uniqueURL)
        playerStats = response.json()
        print("Downloading stats for Player ID: " + str(player) + " - " + playerStats['people'][0]['fullName'])
        finalData['teams'].append(playerStats['people'][0])
        bar()

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

input("Press [ENTER] to close this window!")
"""