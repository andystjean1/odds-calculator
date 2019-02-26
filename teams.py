#holds the structure for a teams
import statistics

abbrevs= {
    "ATL":"Hawks",
    "BKN":"Nets",
    "BOS":"Celtics",
    "CHA":"Hornets",
    "CHI":"Bulls",
    "CLE":"Cavaliers",
    "DAL":"Mavericks",
    "DEN":"Nuggets",
    "DET":"Pistons",
    "GS":"Warriors",
    "HOU":"Rockets",
    "IND":"Pacers",
    "LAC":"Clippers",
    "LAL":"Lakers",
    "MEM":"Grizzlies",
    "MIA":"Heat",
    "MIL":"Bucks",
    "MIN":"Timberwolves",
    "NOP":"Pelicans",
    "NYK":"Knicks",
    "OKC":"Thunder",
    "ORL":"Magic",
    "PHI":"76ers",
    "PHX":"Suns",
    "POR":"Trail Blazers",
    "SAC":"Kings",
    "SA":"Spurs",
    "TOR":"Raptors",
    "UTA":"Jazz",
    "WAS":"Wizards",
}

class Team(object):

    def __init__(self, name, lfs):
        self.name = name
        self.last_five_scores = lfs

    def display_team(self):
        print(self.name, self.last_five_scores)

    def is_favorite(self, abv):
        return self.name == abbrevs[abv]

    def calc_average_score(self):
        return statistics.mean(self.last_five_scores)
