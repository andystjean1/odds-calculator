import requests
from bs4 import BeautifulSoup

def get_urls():
    url="http://www.espn.com/nba/"
    resp = requests.get(url)
    if(resp.status_code != 200):
        print("bad stauts code ", resp.status_code)
        quit()

    soup = BeautifulSoup(resp.content, 'html.parser')

    scoreboard = soup.find('div', attrs={'class':'scoreboard-content'})

    print(scoreboard.prettify())


if __name__ == '__main__':
    get_urls()
