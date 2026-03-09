# PLAYER STATE

class newPlayer:
    def __init__(self):
        #default values
        self.name = name
        self.gender = None
        self.favorite_color = favorite_color
        self.bag = bag
        #call Inv class
        self.money = 0
        self.charType = charType
        #inv capacity
        self.cleanliness = 100
        self.fullness = 100
        self.

    def get_name(player):
        print("\nType your character’s name, then press enter:")
        name = input("> ")
        self.name = name
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
class Bag:
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
        #wrap this in a class
        print(f"\n** {player['bag']} added to inventory. **")
        print(f"You now have ${player['money']}.")
