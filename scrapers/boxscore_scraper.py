import requests
from bs4 import BeautifulSoup
from scrapers.game_scraper import DailyGameScraper


class DailyBoxscoreScraper:

    def __init__(self, daily_url):
        self.base_url = 'https://www.sports-reference.com'
        self.daily_url = daily_url
        self.soup = self.get_soup()

    def get_box_urls(self, url):
        game_urls = DailyGameScraper(self.daily_url).get_game_urls()
        return game_urls

    def get_soup(self, url):
        final_url = self.base_url + url
        r = requests.get((final_url))
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    def get_players(self):



