import random

playing = False

chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

suits = ("H", "A", "S", "D")
ranking = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
card_val = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print (self.suit + self.rank)

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = " "

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

            return "The hand has %s " %hand_comp

    def card_add(self,card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]
