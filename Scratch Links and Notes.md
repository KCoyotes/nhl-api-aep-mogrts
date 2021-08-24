# Scratch links and notes:

-------------------------------------
https://statsapi.web.nhl.com/api/v1/
-------------------------------------


https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster
https://statsapi.web.nhl.com/api/v1/teams/53/roster
https://statsapi.web.nhl.com/api/v1/teams/53/?expand=team.roster?hydrate=stats(splits=statsSingleSeason)

https://statsapi.web.nhl.com/api/v1/people/8473548
https://statsapi.web.nhl.com/api/v1/people/8473548?hydrate=stats(splits=statsSingleSeason)


//Kachina/Share/Github Projects/nhl-api-aep-mogrts

filePath = "//Kachina/Share/Github Projects/nhl-api-aep-mogrts/Main.js";
value = $.evalFile(filePath);

value;

    with open('API_Stats.json', 'a', encoding='utf-8') as f:
        json.dump(playerStats, f, ensure_ascii=False, indent=4)