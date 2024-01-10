#Author: Minh Nguyen
#Date: 10/19/2023
#Purpose: Card class

# Define a Python class called Card to represent playing cards
class Card:
# Constructor for initializing a card object
    def __init__(self, values, suits):
        # Check the values parameter and set the 'value' attribute
        #In each suit, there are 13 card values:
        # cards with numbers 1 through 10, the Jack (11), the Queen (12), and the King (13).
        if values >=1 and values <= 10:
            self.value = values
        elif values == 11:
            self.value = "Jack"
        elif values == 12:
            self.value = "Queen"
        elif values == 13:
            self.value = "King"

        # Check the suits parameter and set the 'suit' attribute
        #There are four suits of cards: clubs, spades, diamonds, and hearts.
        if suits == 1:
            self.suit = "clubs"
        elif suits == 2:
            self.suit = "spades"
        elif suits == 3:
            self.suit = "diamonds"
        elif suits == 4:
            self.suit = "hearts"

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)