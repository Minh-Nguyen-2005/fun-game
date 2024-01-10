#Author: Minh Nguyen
#Date: 10/19/2023
#Purpose: Deck class

from random import randint
from card import Card

#A standard deck has 52 cards: one of each value, for each suit. (We ignore the Joker.)
class Deck:
    def __init__(self):
        self.card_list = []

    def add_standard_cards(self): #Add the 52 standard cards to the new deck.
        for suits in range(1, 5):
            for values in range(1, 14):
                self.card_list.append(Card(values, suits))

    def shuffle(self): #reorder (shuffle) the card list by looping over the list,
        # swapping each item into a random location.
        for i in range(0, len(self.card_list)):
            random = randint(0, len(self.card_list) - 1)
            #pick a random number between the first and the last index in the card list.
            temp = self.card_list[i]
            self.card_list[i] = self.card_list[random]
            self.card_list[random] = temp

    def deal(self, last_cards): #Create a new tiny Deck of cards called hand, made up
#   of the last five cards in deck.  The deal method should
#   also remove those last five cards from "deck".
        hand = Deck()
        for i in range(1, last_cards + 1):
            card = self.card_list.pop() #removes the last item from a list
            # and returns the value of that item.
            hand.card_list.append(card)
        return hand

    def __str__(self):
        return self.card_list