import random

class Card:
    def __init__():
        self.cards = []
        self.suit = suit
        self.value = value

    def __str__():
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return str(self)
       
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Club", "Diamonds", "Hearts", "Spades"]
        values = ["King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace"]
        for suit in suits:
            for value in values:
                self.cards.append(Card)

    def __len__(self):
        return len(self.cards)
     
    def __str__(self): 
        return f"Deck with {len(self.cards)} cards"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        drawn = []
        for _ in range(n):
            if self.cards:
                drawn.append(self.cards.pop())
        return drawn

    #used in looping
    def reset(self):
        self.cards.clear()
        suits = ["Club", "Diamonds", "Hearts", "Spades"]
        values = ["King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

  

    def discard_cards(self, cards): 
        self.discard.extend(cards) 
        # don't forget: hand.clear() when clearning hand
        
    def _reshuffle_from_discard(self): 
        self.cards = self.discard 
        self.discard = [] self.shuffle()


def main():
    #sdeck = standard.deck (no joker)
    sdeck = Deck()
    sdeck.shuffle()

    hand = sdeck.draw(4)

    print("Your hand:")
    for card in hand:
        #print(" •", card)
        print(Card)

    print("\nCards remaining in deck:", len(sdeck))


main()