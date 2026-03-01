def save_game(player, filename="savefile.json"): 
    with open(filename, "w") as f: 
        json.dump(player, f, indent=4) 
        print("\nGame saved.")

def load_game(filename="savefile.json"):             
    with open(filename, "r") as f: 
         #player = json.load(f)
        displayData = json.load(f)
        print(displayData)

class Flags:
    def __init__(self):
        self.flags = []

    def addFlag(self):
        if flag is not in flags:
            self.flags.append(flag)
            return flags

class Save:
    def __init__(self):
        self.save = []

    def __str__(self):
        return f"Event flags: {save}"

    
    def save_game(flags, filename="savefile.json"): 
    with open(filename, "w") as f: 
        json.dump(flags, f, indent=4) 
        print("\nGame saved.")
    


    