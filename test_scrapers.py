from scrapers import game_scraper

URL = 'https://www.sports-reference.com/cbb/boxscores/index.cgi?month=12&day=15&year=2020'

d = game_scraper.DailyGameScraper(URL)

# print(d.get_teams())
# print(len(d.get_teams()))
# print(d.get_scores())
print(len(d.get_scores()))

# z = zip(d.get_teams(), d.get_scores())
#
# for i in z:
#     print(i)

print(len(d.get_game_urls()))