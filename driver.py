import get_odds as GO
from games import Game
from teams import Team
import requests
from bs4 import BeautifulSoup
import re

url="http://www.espn.com/nba/game?gameId=401071580"

games = []

if __name__ == '__main__':
    resp = requests.get(url)
    if(resp.status_code != 200):
        print("bad status code bye ", resp.status_code)
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
