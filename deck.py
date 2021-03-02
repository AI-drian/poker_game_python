from card import Card
from player import Player
import random

class Deck:

    def __init__(self):
        '''
        This is the constructor
        '''
        self.cards = []
        self.build()
    
    def build(self):
        '''
        Method for creating a deck with 52 cards
        '''
        for c in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 13):
                self.cards.append(Card(c, v))
    
    def show(self):
        '''
        Method to display the deck "To String"
        '''
        for c in self.cards:
            c.show()

    def shuffle(self):
        '''
        Method that shuffles the deck
        '''
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        print("\n The deck has been shuffled! \n")
   
    def draw_card(self):
        '''
        This method draws one (1) card
        '''
        return self.cards.pop()

    def number_of_cards_in_deck(self):
        '''
        This method calculates number of cards thats in the deck
        '''
        x = 0
        for c in self.cards:
            x += 1
        print(f"Number of cards in deck: {x}")  


             