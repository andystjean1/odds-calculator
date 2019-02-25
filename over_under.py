import requests
from bs4 import BeautifulSoup
import re

url="http://www.espn.com/nba/game?gameId=401071571"

resp = requests.get(url)
if(resp.status_code != 200):
    print("bad status code bye ", resp.status_code)
    quit()

soup = BeautifulSoup(resp.content, 'html.parser')

scores = soup.find_all('td', attrs={'class':'score', 'colspan':'6'})
over_under = scores[1]

past_games = soup.find('div', attrs={'class':'tab-content sub-module__parallel'})
teams = past_games.find_all('article')

test = teams[1]

table = test.find('div', attrs={'class':'content'}).find('tbody')
name = test.find('header', attrs={'class':'border'})


scores=[]

for tr in table:
    data = tr.find_all('td')
    score = data[-1].text
    win_loss = score[0]
    totals = score[1:].split('-')

    print(totals)




    totals = list(map(int, totals))

    if(win_loss == 'W'):
        scores.append(max(totals))
    else:
        scores.append(min(totals))

print(test.text[:13], scores)
