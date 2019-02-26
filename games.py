

# holds the logic and structure for a game
class Game(object):

    def __init__(self, over_under, spread):
        self.over_under = over_under
        self.spread = spread
        self.favorite = None
        self.underdog = None


    def __str__(self):
        sprd = "Spread: " + self.spread
        ov_un = "Over-Under: " + self.over_under
        return sprd + "\n" + ov_un

    def display_game(self):
        self.favorite.display_team()
        self.underdog.display_team()
        print("Over-Under: ", self.over_under)
        print("Spread: ", self.spread)
