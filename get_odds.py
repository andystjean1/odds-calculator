import requests
from bs4 import BeautifulSoup
import re
import statistics

url="http://www.espn.com/nba/game?gameId=401071571"


def get_over_under(soup):
    scores = soup.find_all('td', attrs={'class':'score', 'colspan':'6'})
    return int(re.search(r'\d\d\d', scores[1].text).group())

def get_average_scores(team):
    #find the table and list each data row
    table = team.find('div', attrs={'class':'content'}).find('tbody')

    #find the name of the team
    name = team.find('header', attrs={'class':'bordered'})
    name = re.search(r'^\w+ \w+ L|^\w+ L', name.text).group()[:-2]

    scores=[]
    for tr in table:
        data = tr.find_all('td')
        score = data[-1].text
        win_loss = score[0]

        #remove overtime listing and split scores
        cleaned_score = re.search(r'\d+-\d+', score[1:]).group()
        totals = cleaned_score.split('-')
        totals = list(map(int, totals))

        #if Win get max score, if Loss get min score
        if(win_loss == 'W'):
            scores.append(max(totals))
        else:
            scores.append(min(totals))

    #calculate the avergae of scores and return
    avg = statistics.mean(scores)
    print(name, scores, avg)
    return avg

#MAIN METHOD
if __name__ == "__main__":
    print("im the main in get_odds.py")
