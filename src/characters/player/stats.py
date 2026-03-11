import time

# health stats: fullness, cleanliness, regularity
# career paths: logistics, sales, security, politics, transportation, education, hospitality, philanthropy
# social groups: bon vivant, streetwise, intellectual
# gigs: pizza delivery, errand runner, task contributor

# flags: unscrambled_eggs, 

# time
# every 5 minutes of gameplay clock, stats drop by: 
# fullness - 10 percent. cleanliness - 2 percent. 
# nature calling - 5 percent. for 1 game hour after eating or drinking,
# nature calling drops by 25 percent every 5 minutes
# needs timer pauses during interactions with other players and during certain scenarios (needs_timer == "OFF")

class Bar:
    def __init__:
        self.fullness = 100
        self.cleanliness = 100
        self.nature_calling = 100 

    def __str__:
        return f"Fullness: {self.fullness}"


#logic

#if self.fullness > 25:
    #print("\nGetting hungry.\n")

# if self.cleanliness > 25:
    #print("\nCleanliness level low. Shower soon.")

# if self.nature_calling > 25:
    #print("\nUh oh, nature calls fast!\n")

# if self.fullness = 0:
    # pass out, go to hospital
    # pay $100 to get out.

# if self.cleanliness = 0:
    #print("\P-U! You stink!")

# if self.nature_calling = 0:
    # use it on yourself. 
    # other sims comment on it and bring it up in the future. 
    # after repeated offenses, sim gets negative reputation.
    # !'s appear around player representing other characters' reaction
    #print("Oh, no!\nYou just went on yourself!")
