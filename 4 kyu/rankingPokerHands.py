class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]
    RANK = ["Highcard", "Pair", "Two pairs", "Three of a kind", "Straight", "Flush"]

    def __init__(self, hand):
        self.hand = [i for i in hand.split()]

    def compare_with(self, other):
        self.other = [i for i in other.split()]
        if self.hand == self.other:
            return self.RESULT[1]
        return self.RESULT[0]

    def get_rank(self, karts):
        if


hand = "KS AS TS QS JS"

player = PokerHand(hand)
print(player.hand)
print(player.compare_with(hand))

# player, opponent = PokerHand(hand), PokerHand(other)
# "Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
# "Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
# "Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
# "4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
# "Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
# "Highest flush wins",  "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
# "Flush wins of straight", "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
# "Equal straight is tie", "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
# runTest("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
# "3 Of a kind wins of two pair",  "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
# runTest("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
# runTest("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
# runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
# runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
# runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
# runTest("Equal cards is tie",		          "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")