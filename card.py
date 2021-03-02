
class Card:
    def __init__(self, color, value):
        '''
        This is the constructor
        '''
        self.color = color
        self.value = value

    def show(self):
        '''
        Method to show card "To String"
        '''
        print(f" {self.value} of {self.color}")
     
     