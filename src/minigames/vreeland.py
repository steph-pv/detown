# import flags from save

class Vreeland:
    def __init__(self):
        self.name = name

    ### VREELAND INTRO
    def hotel(player):
        if Vreeland not in flags:
            time.sleep(2)
            print("\nYou just got off of a phone call and learned that that your hotel was overbooked--that deal was too good to be true!--and that your refund is days away at best (thank you, EZ-Pay). What are you going to do?")
            print("1. Sleep on a park bench tonight")
            print("2. Find a new hotel")

            while True:
                choice = input("> ")
                if choice == "1":
                    print("Get real.")
                elif choice == "2":
                    print("Time to make some phone calls.")
                    return Vreeland(player)
                else:
                    print("Invalid choice.")

    def Vreeland(player):
        time.sleep(2)
        print('\nAs compensation, you\'ve been offered a complimentary stay at the historic Vreeland hotel, which boasts an in-house restaurant, a dance club, and in-room jacuzzi tubs.\n\nAccording to the map, it\'s only a few minutes\' walk from the transit station.')
        time.sleep(2); print('\nAs you make your way there, you hear the glide of a sky train above you. You ought to ride that sometime!'); time.sleep(2); print('\nRounding the block, you spot the half-open door to the hotel restaurant and poke your head in. It\'s got all the markings of a classic American diner, and the charming, unmistakable stench of cut onions and ground chili wash over you (and maybe even stick around a little).')
        time.sleep(2); print('\nFinally, you arrive at the entrance doors of the Vreeland Hotel. You step inside, and, immediately, your breath is taken away by the gilded gold walls, sky-high ceiling, and what you can make of the stunning marble floors beneath residual shoe grime. It\'s very Art Deco, very old Hollywood. It looks like something out of a movie... made fifty-plus years ago.'); time.sleep(1); print('Hauntingly beautiful, suspiciously empty, as if no one has been there in days. You look for a receptionist, but there\'s no one at the desk, or around at all.'); time.sleep(1); print("\nYou're looking around to see if you can find anyone, when you see a beautiful, moody bar area just off the lobby. You walk over there to get a closer look, but it's just as quiet as the rest of the place.\n\nSuddenly, you become aware of your thirst. When did you last have some water? It looks like there's plenty to drink here..."); time.sleep(1)

        while True:
            print("\n1. Call for someone.")
            print("2. Help yourself.\n")
            choice = input("> ")

            if choice == "1":
                print("\'Hello?\'")
                print("\nOh! Someone is coming!")
                return player

            elif choice == "2":
                if player["charType"] == 2:
                    roll = random.randint(1, 6)
                    if roll % 2 == 0:
                        print("\nNevermind! Someone is coming!")
                    else:
                        print("\nYour pour yourself a glass of Orange Fizz. Mmm. Tastes good.")
                        time.sleep(1.5)
                        print("\nOh! Someone is coming!")
                else:
                    print("\nNevermind! Someone is coming!")
                    return player

            else:
                print("\nInvalid choice.")

    ### (almost) all other Vreeland activity
