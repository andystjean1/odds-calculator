

# holds the logic and structure for a game
class Game(object):

    def __init__(self, over_under, spread):
        self.over_under = over_under
        self.spread = float(spread)
        self.favorite = None
        self.underdog = None

    def __str__(self):
        sprd = "Spread: " + self.spread
        ov_un = "Over-Under: " + self.over_under
        return sprd + "\n" + ov_un

    # evaluate the two teams avg scores and see if its over or under
    def check_over_under(self):
        print("Evaluating the Over-Under", "-" *20)
        total = self.favorite.calc_average_score() + self.underdog.calc_average_score()
        print("Over-Under: ", self.over_under)
        print("Total: ", total)

        if(total > self.over_under):
            print("bet the over")
        elif(total < self.over_under):
            print("bet the under")
        else:
            print("bet push")

    def check_spread(self):
        print("Evaluating the Spread", "-" *20)
        #get average score from last 5 games
        fav_total = self.favorite.calc_average_score()
        dog_total = self.underdog.calc_average_score()

        #check favorite is greater than underdog
        if(fav_total > dog_total):
            #caluclate spread totals
            fav_total -= self.spread
            dog_total += self.spread

            if(fav_total > dog_total):
                print('Favorite: ', fav_total)
                print('Underdog: ', dog_total)
                print('bet to cover the spread')

            else:
                print('Favorite: ', fav_total)
                print('Underdog: ', dog_total)
                print('bet against the spread')

        else: #favorite total is less than underdog total
            print('Favorite: ', fav_total)
            print('Underdog: ', dog_total)
            print('bet against the spread')

    #prints the game to the screen
    def display_game(self):
        self.favorite.display_team()
        self.underdog.display_team()
        print('-'*50)
