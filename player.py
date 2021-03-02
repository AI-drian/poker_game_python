

class Player:

    def __init__(self, name, age, title):
        '''
        This is the constructor
        '''
        self.name = name
        self.age = age
        self.title = title
        self.hand = []
    
    def draw(self, deck):
        '''
        Function for drawing 1 card
        '''
        self.hand.append(deck.draw_card())
        return self

    def draw_five(self, deck):
        '''
        Funnction for drawing five cards
        '''
        x = 0 
        while x < 5:
            self.hand.append(deck.draw_card())
            x += 1
        print(f"5 cards given to: {self.name}")
        return self

    def show_hand(self):
        '''
        function to display all cards in player hand
        '''
        if len(self.hand) == 0:
            print(f" {self.name}s hand is empty")
        else:  
            print(f"\n {self.name}s hand: ")
            for card in self.hand:
                card.show()
                print(" ")

    def show_player(self):
        '''
        Function to show player "To String"
        '''
        print(f"Player: {self.name}, Age: {self.age}, Title: {self.title}\n")

    def total_value_in_hand(self):
        '''
        This function calculates the total value of cards in hand
        '''
        total = 0
        for card in self.hand:
            total += card.value
        print(f"Total card value in {self.name}s hand: {total}\n")

    def toss_lowest_cards(self):
        '''
        This function will find and toss the two lowest cards from one players hand. I guess this could have been done nicer.
        ''' 
        lowest_card = []

        # Sorting the cards in the players hand by value from lowest to highest. 
        for card in self.hand:
            lowest_card.append(card.value)
        lowest_card.sort()
        print(f" {self.name} decides to toss: {lowest_card[0]} and {lowest_card[1]} \n")

        # Removing the two lowest cards (index 0 and 1)
        for card in self.hand:
            if card.value == lowest_card[0]:
                self.hand.remove(card)

        for card in self.hand:
            if card.value == lowest_card[1]:
                self.hand.remove(card)              
        self.show_hand()            
    
    def toss_all_cards(self):
        '''
        This function will make the player toss all cards from their hand
        '''
        self.hand.clear()

        #for c in self.hand:
        #    self.hand.pop()


            
        
