from card import Card
from deck import Deck
from player import Player

deck = Deck()

slim = Player("Slim", 30, "World Champion 2005")
luke = Player("Luke", 35, "Malmö-open 2016")


print("\n---------------Poker Time!---------------\n")

Deck.show(deck)

Deck.shuffle(deck)
Deck.show(deck)

print("\n----------------The players are----------------")
Player.show_player(slim)
Player.show_player(luke)

Player.draw_five(slim, deck)
Player.show_hand(slim)
Player.toss_lowest_cards(slim)

Player.draw_five(luke, deck)
Player.show_hand(luke)
Player.toss_lowest_cards(luke)

Player.draw(slim, deck)
Player.draw(slim, deck)
Player.draw(luke, deck)
Player.draw(luke, deck)

Player.show_hand(slim)
Player.total_value_in_hand(slim)
Player.show_hand(luke)
Player.total_value_in_hand(luke)

Deck.number_of_cards_in_deck(deck)

Player.toss_all_cards(slim)
Player.show_hand(slim)
