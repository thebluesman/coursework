import random

playing = False

chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

suits = ("H", "C", "S", "D")
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

            return "The hand has %s" %hand_comp

    def card_add(self,card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_value(self):

        if self.ace == True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self,hidden):

        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self,deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = " "

        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has " + deck_comp

def make_bet():

    global bet
    bet = 0

    print "Bet amount?"

    while bet == 0:
        bet_comp = raw_input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print "Invalid bet. You have only " + str(chip_pool) + " chips remaining"

def deal_cards():

    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet

    deck = Deck()

    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand: Press h or s!"

    if playing = True:
        print "Fold, sorry!"
        chip_pool -= bet

    playing = True
    game_step()

def game_step():

    print " "
    print "Player hand is ",
    player_hand.draw(hidden=False)

    print "Player hand total is " + str(player_hand.calc_value())

    print "Dealer hand is ",
    dealer_hand.draw(hidden=True)

    if playing == False:
      print "Dealer hand total is: " + str(dealer_hand.calc_value())
      print "Chip total is: " + str(chip_pool)

    else:
        print "With another card hidden"

    print result

    player_input()

def game_exit():

    print "Thank you for playing!"
    exit()

def player_input():

    plin = raw_input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print "Invalid entry. Please input either h, s, q or d"
        player_input()

def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print statement

deck = Deck()

deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()

deal_cards()