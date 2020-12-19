import requests
from bs4 import BeautifulSoup
from scrapers.game_scraper import DailyGameScraper

URL = 'https://www.sports-reference.com/cbb/boxscores/index.cgi?month=12&day=15&year=2020'
BASE_URL = 'https://www.sports-reference.com'

gs = DailyGameScraper(URL)
urls = gs.get_game_urls()
end = urls[0]

f_url = BASE_URL + end
r = requests.get(f_url)
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup)

box = soup.find(id='boxes')
stats_table = box.findAll('tbody')
team1_stats = stats_table[:2]
team2_stats = stats_table[2:]
team1_players = []
# print(team1_stats[0].findAll('th'))
# for i in team2_stats[0].findAll(lambda tag: tag.name == 'th' and 'left' in tag.get('class')):
#     print(i)
#     if i.text != 'Reserves':
#         # print(i.text)
#         team1_players.append(i.text)
# print('\n')
# print(team2_stats)
# s = team1_stats[0].findAll('td')
# for i in s:
#     print(i)
all_player_stats = []
id = 1
for s in team1_stats:
    r = s.findAll(lambda tag: tag.name == 'tr' and not tag.get('class'))
    for i in r:
        boxscore = {}
        player_stats = i.findAll('td')
        full_name = i.find('th').text
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1:]
        boxscore['id'] = id
        id += 1
        boxscore['first_name'] = first_name
        boxscore['last_name'] = " ".join(last_name)
        for x in player_stats:
            boxscore[x['data-stat']] = x.text
        all_player_stats.append(boxscore)
        if id == 11:
            id = 1



for i in all_player_stats:
    # print(i)
    if i['id']