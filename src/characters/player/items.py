# items that player receives NOT from markets, etc
# read from items dictionary located in item_data file

# MAP
def getMap():
    time.sleep(2); print("\nStepping off the bus, you\'re greeted by a mural of a classic muscle car across the cement wall if the station."); time.sleep(1); print("You take a moment to admire it."); print("\n***"); time.sleep(2)
    print("\nA friendly transit employee walks up to you and hands you a CITY MAP."); time.sleep(1); print('Thank you!\nThat\'s going to come in handy!')
    #call item and inventory class
    #map = Item()
    #map.Inventory()
    time.sleep(2); print('\nNow, let\'s find our hotel...'); time.sleep(3)
    return player

class Item:
    #modify to read contents from a dictionary
    def __init__(self):
        self.name = name
        #description
        self.desc = desc
        self.rarity = rarity
        self.price = price

    def __str__(self):
        return f"{item}: {desc}"
            
class Inventory:
    def __init__(self):
        self.items = []
        self.capacity = capacity

    def addToInventory(self):
        if self.capacity is None or len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item} added to inventory.")
            return True

    def removeFromInventory(self):

    
