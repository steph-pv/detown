import random
from deck import standard_deck

def deal4(deck):
    global working_deck = standard_deck.copy()
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
    deal4(standard_deck)

main()