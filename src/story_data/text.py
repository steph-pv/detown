# CHARACTER CREATION

def get_name(player):
    print("\nType your character’s name, then press enter:")
    name = input("> ")
    player["name"] = name
    return ask_gender(player)

def ask_gender(player):
    while True:
        print("\nEnter m for male or f for female:")
        gender = input("> ").lower()
        if re.fullmatch(r"m|male", gender, re.IGNORECASE):
            player["gender"] = "male"
            time.sleep(1)
            print("\nNice to meet you!")
            time.sleep(1)
            return fav_color(player)
        elif re.fullmatch(r"f|female", gender, re.IGNORECASE):
            player["gender"] = "female"
            time.sleep(1)
            print("\nNice to meet you!")
            time.sleep(1)
            return fav_color(player)
        else:
            print("Invalid input.")

def fav_color(player):
    while True:
        choice = str(input(
            "\nWhat is your favorite color?\n"
            "1. Red\n2. Blue\n3. Green\n4. Pink\n5. Orange\n6. Purple\n7. White\n8. Black\n"
        )).strip()

        colors = {
            "1": "red", "2": "blue", "3": "green", "4": "pink",
            "5": "orange", "6": "purple", "7": "white", "8": "black"
        }

        if choice in colors:
            player["favorite_color"] = colors[choice]
            return choose_bag(player)
        else:
            print("Invalid choice. Try again.")

# BAG SELECTION

def choose_bag(player):
    time.sleep(5)
    print("\nWelcome to DeTown!")
    time.sleep(3)
    print("\nAfter months of preparation, years of planning, and hours of trail mix, your bus has arrived at the King-Parks Transit Station in downtown De.")
    time.sleep(2)
    print("\nYour new life is about to begin! Before you leave, make sure to grab your bag…")
    time.sleep(1)

    while True:
        bag = input(
            "\nWhich one is yours?\n"
            "1. Monogrammed designer glider\n"
            "2. Black leather duffel bag\n"
            "3. Reusable grocery tote\n"
        )

        if bag == "1":
            player["bag"] = "Monogrammed designer glider"
            player["charType"] = 1
            player["inventory"].append(player["bag"])
            player["money"] += 500
            break

        elif bag == "2":
            player["bag"] = "Black leather duffel bag"
            player["charType"] = 2
            player["inventory"].append(player["bag"])
            player["money"] += 1000
            break

        elif bag == "3":
            player["bag"] = "Reusable grocery tote"
            player["charType"] = 3
            player["inventory"].append(player["bag"])
            player["money"] += 3500
            break

        else:
            print("Invalid choice. Try again.")

    print(f"\n** {player['bag']} added to inventory. **")
    print(f"You now have ${player['money']}.")

    def hotel(player):
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
            return player
        else:
            print("Invalid choice.")

### VREELAND INTRO

def Vreeland(player):
    time.sleep(2)
    print('\nAs compensation, you\'ve been offered a complimentary stay at the historic Vreeland hotel, which boasts an in-house restaurant, a dance club, and in-room jacuzzi tubs.\n\nAccording to the map, it\'s only a few minutes\' walk from the transit station.')
    time.sleep(2)

    print('\nAs you make your way there, you hear the glide of a sky train above you. You ought to ride that sometime!')
    time.sleep(2)

    print('\nRounding the block, you spot the half-open door to the hotel restaurant and poke your head in. It\'s got all the markings of a classic American diner, and the charming, unmistakable stench of cut onions and ground chili wash over you (and maybe even stick around a little).')
    time.sleep(2)

    print('\nFinally, you arrive at the entrance doors of the Vreeland Hotel. You step inside, and, immediately, your breath is taken away by the gilded gold walls, sky-high ceiling, and what you can make of the stunning marble floors beneath residual shoe grime. It\'s very Art Deco, very old Hollywood. It looks like something out of a movie... made fifty-plus years ago.')
    time.sleep(1)

    print('Hauntingly beautiful, suspiciously empty, as if no one has been there in days. You look for a receptionist, but there\'s no one at the desk, or around at all.')
    time.sleep(1)

    print("\nYou're looking around to see if you can find anyone, when you see a beautiful, moody bar area just off the lobby. You walk over there to get a closer look, but it's just as quiet as the rest of the place.\n\nSuddenly, you become aware of your thirst. When did you last have some water? It looks like there's plenty to drink here...")
    time.sleep(1)

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
