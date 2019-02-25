import requests
from bs4 import BeautifulSoup
import re
import statistics

url="http://www.espn.com/nba/game?gameId=401071571"


def get_over_under(soup):
    scores = soup.find_all('td', attrs={'class':'score', 'colspan':'6'})
    return int(re.search(r'\d\d\d', scores[1].text).group())

def get_average_scores(team):
    #put inside for loop for each team
    table = team.find('div', attrs={'class':'content'}).find('tbody')
    name = team.find('header', attrs={'class':'bordered'})
    name = re.search(r'^\w+ \w+ L|^\w+ L', name.text).group()[:-2]

    scores=[]

    for tr in table:
        data = tr.find_all('td')
        score = data[-1].text
        win_loss = score[0]

        cleaned_score = re.search(r'\d+-\d+', score[1:]).group()

        totals = cleaned_score.split('-')

        totals = list(map(int, totals))

        if(win_loss == 'W'):
            scores.append(max(totals))
        else:
            scores.append(min(totals))

    avg = statistics.mean(scores)
    print(name, scores, avg)
    return avg

#MAIN METHOD
if __name__ == "__main__":
    resp = requests.get(url)
    if(resp.status_code != 200):
        print("bad status code bye ", resp.status_code)
        quit()

    soup = BeautifulSoup(resp.content, 'html.parser')
    over_under = get_over_under(soup)

    #find past 5 games
    past_games = soup.find('div', attrs={'class':'tab-content sub-module__parallel'})
    teams = past_games.find_all('article')

    total = 0.0

    for t in teams:
        total += get_average_scores(t)

    print('Over/Under: ', over_under)
    print('Total score: ', total)

    if(total > over_under):
        print("bet the over")
    elif(total < over_under):
        print('bet the under')
    else:
        print('its a push')
