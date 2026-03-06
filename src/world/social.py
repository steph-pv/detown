# social dynamics

#In general: +2 social points per positive interaction

#bon-vivant personalities: like talking about travel (OE), like exclusive clubs (Y/N)
# 
# Ask about: travel, exclusive clubs, food, work, hobbies, fashion, 
# underground, 
# Insult, argue with, grapple with (intellectuals), 
# ask about school, public transportation, 

from player import*
from characters import*

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

    Questions = {“question”: “Ask about reading.” {“charType”: “1” {“response”: {“I’m a /total/ tabloid junkie.”, “Duh! Don’t we all?”}
    “charType”: “2” {“response”: “Sure, I do that sometimes, yeah.”}, {“response”: “C’mon man, get real.”},
    "charType": "3" {"response: {"I thought you’d never ask!"}, {"I can spend hours reading programming documentation."},
    "believer"
    #so on and so forth
    
    #ask a charType 3 about a book three times in a conversation and receive a book
    
class Convo:
    def __init__(self):
