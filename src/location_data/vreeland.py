#from characters import meetjuwaiyrah

def leaveRoom():
    print("Do you want to leave your room?")
    c = input("1. Stay here/n2. Go to the lobby/n3. Go outside")
    if c == "1":
        return c
        #redecorate room, rest, invite someone over (flags), do nothing (time.sleep(10))
    elif c == "2":
        return c
        #lobby()
    elif c == "3":
        return c #map or list with can_go locations (can_go flag after visiting)
    else:
        leaveRoom()

def rest():
#rest until evening, rest overnight, rest until morning. 
#evening: 5pm game time. 1 hr until day markets close. 2 hours before night markets open. 
#overnight: rest until sleep is fully restored. until morning: rest until 5am.
    print("sleep tight.")

def redecorate():
#dump inventory: on the table (2 items max) on the floor. # of items on the floor have consequences ("wow, your place is really messy.")
    print(f"Your inventory currently contains the following: {inv}")

def invite():
#invite somebody over: can_invite flag, else "But you have no one to call."
#?? why invite someone over? assess your space. if it's to their preference, +2 social points. sims may or may not come over.
    print("But you have no one to call.")
    time.sleep(1)
    invite()

def lobby():
    print("You are in the lobby.")

