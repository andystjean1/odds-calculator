from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
import statistics

nba_url="http://www.espn.com/nba/"

#get the list of todays games from espn
def get_game_urls():
    driver = webdriver.Chrome()
    driver.get(nba_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    scoreboard = soup.find('div', attrs={'class':'scoreboard active'})
    game_urls = scoreboard.find_all('a', attrs={'class':'cscore_link'})
    return [x['href'] for x in game_urls]


def get_over_under(soup):
    #Check if scores is None
    try:
        scores = soup.find_all('td', attrs={'class':'score', 'colspan':'6'})
        return int(re.search(r'\d\d\d', scores[1].text).group())
    except IndexError:
        print("I THINK THIS GAME HAS STARTED!!!")
        return -1

def get_team_name(team):
    #find the table and list each data row
    table = team.find('div', attrs={'class':'content'}).find('tbody')
    #find the name of the team
    name = team.find('header', attrs={'class':'bordered'})
    name = re.search(r'^\w+ \w+ L|^\w+ L', name.text).group()[:-2]
    return name

def get_last_five_scores(team):
    #find the table and list each data row
    table = team.find('div', attrs={'class':'content'}).find('tbody')

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
    return scores

#get the spread of the game from the main page
def get_spread(soup):
    teams = soup.find('div', attrs={'class':'competitors'})
    line = teams.find('span', attrs={'class':'line'})
    spread = line.text.split(' ')
    return spread[1][1:]

def get_favorite(soup):
    teams = soup.find('div', attrs={'class':'competitors'})
    line = teams.find('span', attrs={'class':'line'})
    spread = line.text.split(' ')
    return spread[0]


#MAIN METHOD
if __name__ == "__main__":
    urls = get_game_urls()
    for u in urls:
        print(u['href'])
