import random

playing = False

chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

suits = ("H", "A", "S", "D")
ranking = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
card_val = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}