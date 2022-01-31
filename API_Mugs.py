import os
import json
from pathlib import Path
from re import search
import requests
import shutil
import time
import zipfile
from tqdm import tqdm
from alive_progress import alive_bar


os.system('clear')
print("   ____________  ______  _________________")
print("  / ____/ __ \ \/ / __ \/_  __/ ____/ ___/")
print(" / /   / / / /\  / / / / / / / __/  \__ \ ")
print("/ /___/ /_/ / / / /_/ / / / / /___ ___/ / ")
print("\____/\____/ /_/\____/ /_/ /_____//____/  ")
print("                                          ")
print("nhl-api-mugshots | v0.1 Build 20")
print("Scrape Mugshots using NHL's Stats API\n")
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


selectedTeam = list(filter(lambda x:x["abbreviation"]==teamSelect,teams['teams']))
print('Creating headshot directory for ' + selectedTeam[0]['name'] + "...")
folderPath = Path('C:\\' + str(teamSelect)).mkdir(parents=True, exist_ok=True)
folderPath


rosterURL = 'https://statsapi.web.nhl.com/api/v1/teams/' + str(selectedTeam[0]['id']) + '/?expand=team.roster'
teamURL = 'https://statsapi.web.nhl.com/api/v1/teams/' + str(selectedTeam[0]['id']) + '/'


r = requests.get(rosterURL)
t = requests.get(teamURL)

rosterData = r.json()
teamData = t.json()
finalData = {"TIMESTAMP" : timestampStr}
finalData.update(teamData)

copyright=finalData['copyright'].split(". ", 2)
print("\nDISCLAIMER:\n" + copyright[0] + ".\n" + copyright[1] + ".\n" + copyright[2] + "\n")
time.sleep(1)
print(timestampStr + "\n")
time.sleep(1)

finalData['DEBUG'] = timestampStr

uniqueIDs = []
missingList = []

team = rosterData['teams'][0]['roster']['roster']

for roster in team:
    ID = roster['person']['id']
    uniqueIDs.append(ID)

with alive_bar(len(uniqueIDs), length=30, bar='smooth', enrich_print=False) as bar:
    for player in uniqueIDs:
        playerURL = 'https://statsapi.web.nhl.com/api/v1/people/' + str(player)
        response = requests.get(playerURL)
        playerInfo = response.json()
        imageURL = 'https://cms.nhl.bamgrid.com/images/headshots/current/168x168/' + str(player) + '@3x.png'
        print("Downloading headshot for #" + playerInfo['people'][0]['primaryNumber'] + " - " + playerInfo['people'][0]['fullName'] + " (API_ID: " + str(player) + ")")
        response = requests.get(imageURL, stream = True)
        if response.status_code == 200:
            response.raw.decode_content = True
            file_path = Path('C:\\' + str(teamSelect) + '\\' + playerInfo['people'][0]['lastName'] + '_' + playerInfo['people'][0]['firstName'] + '.png')
            with open(file_path,'wb') as f:
                shutil.copyfileobj(response.raw, f)
        else:
            missingPlayer = "#" + playerInfo['people'][0]['primaryNumber'] + " - " + playerInfo['people'][0]['fullName']
            missingList.append(str(missingPlayer))
            print('[ERROR] Unable to download headshot for #' + playerInfo['people'][0]['primaryNumber'] + " - " + playerInfo['people'][0]['fullName'])
        bar()


print("\nDownloads Complete!\n\nAll available headshots were saved to " + 'C:\\' + str(teamSelect) + '\\')
if len(missingList) > 0:
    print("The following players were unable to be downloaded and may need to be cutout manually:",*missingList, sep = "   ")
else: pass

input("\nPress any key to close RosterGEN...")
