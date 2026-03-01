import random
standard_deck = [
    {"suit": "Clubs", "value": "King"},
    {"suit": "Clubs", "value": "Queen"},
    {"suit": "Clubs", "value": "Jack"},
    {"suit": "Clubs", "value": 10},
    {"suit": "Clubs", "value": 9},
    {"suit": "Clubs", "value": 8},
    {"suit": "Clubs", "value": 7},
    {"suit": "Clubs", "value": 6},
    {"suit": "Clubs", "value": 5},
    {"suit": "Clubs", "value": 4},
    {"suit": "Clubs", "value": 3},
    {"suit": "Clubs", "value": 2},
    {"suit": "Clubs", "value": "Ace"}, 
    {"suit": "Diamonds", "value": "King"},
    {"suit": "Diamonds", "value": "Queen"},
    {"suit": "Diamonds", "value": "Jack"},
    {"suit": "Diamonds", "value": 10},
    {"suit": "Diamonds", "value": 9},
    {"suit": "Diamonds", "value": 8},
    {"suit": "Diamonds", "value": 7},
    {"suit": "Diamonds", "value": 6},
    {"suit": "Diamonds", "value": 5},
    {"suit": "Diamonds", "value": 4},
    {"suit": "Diamonds", "value": 3},
    {"suit": "Diamonds", "value": 2},
    {"suit": "Diamonds", "value": "Ace"},
    {"suit": "Hearts", "value": "King"},
    {"suit": "Hearts", "value": "Queen"},
    {"suit": "Hearts", "value": "Jack"},
    {"suit": "Hearts", "value": 10},
    {"suit": "Hearts", "value": 9},
    {"suit": "Hearts", "value": 8},
    {"suit": "Hearts", "value": 7},
    {"suit": "Hearts", "value": 6},
    {"suit": "Hearts", "value": 5},
    {"suit": "Hearts", "value": 4},
    {"suit": "Hearts", "value": 3},
    {"suit": "Hearts", "value": 2},
    {"suit": "Hearts", "value": "Ace"}, 
    {"suit": "Spades", "value": "King"},
    {"suit": "Spades", "value": "Queen"},
    {"suit": "Spades", "value": "Jack"},
    {"suit": "Spades", "value": 10},
    {"suit": "Spades", "value": 9},
    {"suit": "Spades", "value": 8},
    {"suit": "Spades", "value": 7},
    {"suit": "Spades", "value": 6},
    {"suit": "Spades", "value": 5},
    {"suit": "Spades", "value": 4},
    {"suit": "Spades", "value": 3},
    {"suit": "Spades", "value": 2}, 
    {"suit": "Spades", "value": "Ace"}]

def deal4():
    working_deck = standard_deck.copy()
    i = 0
    your_hand = []
    while i < 4 and len(working_deck) > 0:
        r = len(working_deck)
        p = random.randint(0, r - 1)
        c = standard_deck[p]

        your_hand.append(c)
        # print(f"Adding {c["value"]} of {c["suit"]} to your hand.")

        standard_deck.pop(p)
        # print("cards remaining in deck: ", len(standard_deck), /n)
        i = i + 1
        print(c)
    print("cards remaining in deck: ", len(your_hand))
    print("You drew 4 cards.")
    return your_hand

#def draw():

def main():
    deal4()

main()