import get_odds as GO
import requests
from bs4 import BeautifulSoup
import re

url="http://www.espn.com/nba/game?gameId=401071571"



if __name__ == '__main__':
    resp = requests.get(url)
    if(resp.status_code != 200):
        print("bad status code bye ", resp.status_code)
        quit()

    soup = BeautifulSoup(resp.content, 'html.parser')

    over_under = GO.get_over_under(soup)

    #find past 5 games
    past_games = soup.find('div', attrs={'class':'tab-content sub-module__parallel'})
    teams = past_games.find_all('article')

    total = 0.0

    for t in teams:
        total += GO.get_average_scores(t)

    print('Over/Under: ', over_under)
    print('Total score: ', total)

    if(total > over_under):
        print("bet the over")
    elif(total < over_under):
        print('bet the under')
    else:
        print('its a push')
