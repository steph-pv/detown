from characters import meetjuwaiyrah

def leaveRoom():
    print("Do you want to leave your room?")
    c = input("1. Stay here/n2. Go to the lobby/n3. Go outside")
    if c == "1":
        return c
    elif c == "2":
        return c
    elif c == "3":
        return c
    else:
        leaveRoom()

def redecorate():
    print(f"Your inventory currently contains the following: {inv}")