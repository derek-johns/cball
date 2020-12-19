import requests
from bs4 import BeautifulSoup


class DailyGameScraper:

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()
        self.game_table = self.get_game_table()

    def get_soup(self):
        """
        makes a request to url specified when object is created
        :return: beautiful soup object
        """
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    def get_game_table(self):
        """
        finds game table from soup object
        :return: list of all games
        """
        game_table = self.soup.find(id='div_other_scores')
        return game_table

    def get_teams(self):
        """
        parses team names from list of all games
        :return: list of all team names
        """
        all_games = self.game_table.findAll('div', class_='game_summary')
        all_teams = []
        for g in all_games:
            single_game_teams = g.findAll('a')
            t1 = single_game_teams[0].text
            t2 = single_game_teams[2].text
            all_teams.extend([t1, t2])
        return all_teams

    def get_scores(self):
        """
        parses team scores from list of all games
        :return: list of all team scores
        """
        scores = self.game_table.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['right'])
        filtered_scores = [s.text for s in scores if s.text.isdigit()]
        return filtered_scores

    def get_game_urls(self):
        """
        parses boxscore url from list of all games
        :return: list of all boxscore urls
        """
        urls = self.game_table.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['right', 'gamelink'])
        all_urls = []
        for u in urls:
            all_urls.append(u.find('a').get('href'))
        return all_urls

