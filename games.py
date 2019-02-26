

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

    # evaluate the two teams avg scores and see if its over or under
    def check_over_under(self):
        total = self.favorite.calc_average_score() + self.underdog.calc_average_score()
        print("Over-Under: ", self.over_under)
        print("Total: ", total)

        if(total > self.over_under):
            print("bet the over")
        elif(total < self.over_under):
            print("bet the under")
        else:
            print("bet push")

    #prints the game to the screen
    def display_game(self):
        self.favorite.display_team()
        self.underdog.display_team()
        print("Over-Under: ", self.over_under)
        print("Spread: ", self.spread)
