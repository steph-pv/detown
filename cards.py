standard_deck = #no jokers
    [{“suit”: “Clubs”, “value”: “King”},
    {“suit”: “Clubs”, “value”: “Queen”},
    {“suit”: “Clubs”, “value”: “Jack”},
    {“suit”: “Clubs”, “value”: 10},
    {“suit”: “Clubs”, “value”: 9},
    {“suit”: “Clubs”, “value”: 8},
    {“suit”: “Clubs”, “value”: 7},
    {“suit”: “Clubs”, “value”: 6},
    {“suit”: “Clubs”, “value”: 5},
    {“suit”: “Clubs”, “value”: 4},
    {“suit”: “Clubs”, “value”: 3},
    {“suit”: “Clubs”, “value”: 2},
    {“suit”: “Clubs”, “value”: “Ace”}, 
    
    {“suit”: “Diamonds”, “value”: “King”},
    {“suit”: “Diamonds”, “value”: “Queen”},
    {“suit”: “Diamonds”, “value”: “Jack”},
    {“suit”: “Diamonds”, “value”: 10},
    {“suit”: “Diamonds”, “value”: 9},
    {“suit”: “Diamonds”, “value”: 8},
    {“suit”: “Diamonds”, “value”: 7},
    {“suit”: “Diamonds”, “value”: 6},
    {“suit”: “Diamonds”, “value”: 5},
    {“suit”: “Diamonds”, “value”: 4},
    {“suit”: “Diamonds”, “value”: 3},
    {“suit”: “Diamonds”, “value”: 2},
    {“suit”: “Diamonds”, “value”: “Ace”},
    
    {“suit”: “Hearts”, “value”: “King”},
    {“suit”: “Hearts”, “value”: “Queen”},
    {“suit”: “Hearts”, “value”: “Jack”},
    {“suit”: “Hearts”, “value”: 10},
    {“suit”: “Hearts”, “value”: 9},
    {“suit”: “Hearts”, “value”: 8},
    {“suit”: “Hearts”, “value”: 7},
    {“suit”: “Hearts”, “value”: 6},
    {“suit”: “Hearts”, “value”: 5},
    {“suit”: “Hearts”, “value”: 4},
    {“suit”: “Hearts”, “value”: 3},
    {“suit”: “Hearts”, “value”: 2},
    {“suit”: “Hearts”, “value”: “Ace”}, 
    
    {“suit”: “Spades”, “value”: “King”},
    {“suit”: “Spades”, “value”: “Queen”},
    {“suit”: “Spades”, “value”: “Jack”},
    {“suit”: “Spades”, “value”: 10},
    {“suit”: “Spades”, “value”: 9},
    {“suit”: “Spades”, “value”: 8},
    {“suit”: “Spades”, “value”: 7},
    {“suit”: “Spades”, “value”: 6},
    {“suit”: “Spades”, “value”: 5},
    {“suit”: “Spades”, “value”: 4},
    {“suit”: “Spades”, “value”: 3},
    {“suit”: “Spades”, “value”: 2}, 
    {“suit”: “Spades”, “value”: “Ace”}]
    high_ace = 11
    low_ace = 1

def deal4(standard_deck):
    i = 0
    r = 51
    your_hand = []
    while i < 4:
        p = random.randint(0, r)
        s = standard_deck
        c = s.get(p)
        your_hand.append(c)
        print(f”Adding {value} of {suit} to your hand.”)
        print("c = ", c)
        s.pop(p)
        r =-1
        i + 1

#def draw():

def main():
    deal4()

main()