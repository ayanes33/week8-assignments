import random
class Deck:
    def __init__(self):
        self.cards = []
        self.reset()
    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [{'value': value, 'suit': suit} for suit in suits for value in values]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def display(self):
        for card in self.cards:
            print(f"{card['value']} of {card['suit']}")
            
deck = Deck()
deck.shuffle()
hand = Hand()
print("Card Dealer\n")
print(" I have shuffled a deck of 52 cards\n")
num_cards = int(input(" How many cards do you want to deal? "))
for _ in range(num_cards):
    card = deck.deal_card()
    if card:
        hand.add_card(card)
    else:
        print("No more cards to deal!")
   
print("Your Hand: ")
hand.display()
print("There are", (52)-(num_cards), "cards left in the deck")
print("Good luck")
