#import stuff i wrote
import get_odds as GO
from games import Game
from teams import Team

#imported libraries
import requests
from bs4 import BeautifulSoup
import re

base="http://www.espn.com"

games = []

if __name__ == '__main__':

    game_urls = GO.get_game_urls()

    for url in game_urls:

        resp = requests.get(base+url)
        if(resp.status_code != 200):
            print("bad status code bye ", resp.status_code)
            print("url: ", base+url)
            quit()

        soup = BeautifulSoup(resp.content, 'html.parser')

        over_under = GO.get_over_under(soup)
        spread = GO.get_spread(soup)
        game = Game(over_under, spread)

        #find past 5 games
        past_games = soup.find('div', attrs={'class':'tab-content sub-module__parallel'})
        teams = past_games.find_all('article')

        for t in teams:
            squad = Team(GO.get_team_name(t), GO.get_last_five_scores(t))
            if(squad.is_favorite(GO.get_favorite(soup))):
                game.favorite = squad
            else:
                game.underdog = squad


        game.display_game()
        game.check_over_under()
        game.check_spread()
        print('-'*50)
