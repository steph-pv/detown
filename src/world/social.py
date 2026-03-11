from player import *
from characters import *

#decision binary: c = randomint.random(0,7), d = decision_binary[c], if d == "0": index dictionary social object
Class social:
    def __init__(self, character):
        self.name = name
        self.socialtype = socialtype
        self.likes = likes
        self.dislikes = dislikes
        self.industry = industry
        self.job = job
        self.cleanliness = cleanliness
        character.name = name
        character.socialtype = socialtype
        character.likes = likes
        character.dislikes = dislikes
        character.industry = industry
        character.job = job
        character.cleanliness = cleanliness

    def __str__(self, character):
        return f"{self.name} started talking to {character.name}"
    
    def ask(self, character):

class Convo:
    def __init__(self):
