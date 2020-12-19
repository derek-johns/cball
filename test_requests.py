import requests
from bs4 import BeautifulSoup

URL = 'https://www.sports-reference.com/cbb/boxscores/index.cgi?month=12&day=15&year=2020'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

game_table = soup.find(id='div_other_scores')

# game = game_table.find('div', class_='game_summary').findAll('a')
#
# print(game[0].text)
# print(game[2].text)

# all_games = game_table.findAll('div', class_='game_summary')
#
# # print(all_games[0])
#
# teams = all_games[0].findAll('a')
# team1 = teams[0].text
# team2 = teams[2].text
# # print(teams)
# print(team1)
# print(team2)

# scores = game_table.findAll('td', class_='right')

# scores = game_table.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['right'])
#
# # scores = game_table.findAll('td', {'class': 'right'})
#
#
# # print(scores)
# l = [s.text for s in scores if s.text != '\xa0\n\t\t\t']
# # for s in scores:
# #     if s.text != '\xa0\n\t\t\t':
# #         l.append(s.text)
# print(l)

# urls = game_table.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['right', 'gamelink'])
# for u in urls:
#     print(u.find('a').get('href'))

