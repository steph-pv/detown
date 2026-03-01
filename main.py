# -*- coding: UTF-8 -*-

import json
import random
import re
import time
from text import *


# MAIN

def main():
  while True:
    player = player.newPlayer()

    title = 'DeTown!'.title()
    print(title)
    time.sleep(3)

    print("\nEnter s to start:")
    start = input("> ").lower()
    if start != "s":
        return main()

    get_name(player)
    print('\nWhile leaving, a table catches your eye.')
    shop(player)
    hotel(player)
    Vreeland(player)

    print("\nTO BE CONTINUED…")
    print("\nYour final stats:")
    print(player)

    #save_game(player, filename="savefile.json")
    #load_game(filename="savefile.json")

    choice = input("\nPlay again? Enter y for yes or n for no): ").lower() 
    if choice != "y": 
        print("Thanks for playing!") 
        break

main()
