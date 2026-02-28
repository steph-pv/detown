def save_game(player, filename="savefile.json"): 
    with open(filename, "w") as f: 
        json.dump(player, f, indent=4) 
        print("\nGame saved.")

def load_game(filename="savefile.json"):             
    with open(filename, "r") as f: 
         #player = json.load(f)
        displayData = json.load(f)
        print(displayData)