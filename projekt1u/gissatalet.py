'''
gissatalet.py: Ett spel där målet är att gissa det hemliga talet!

COLORS.PY: Color module

__author__  = "Sion"
__version__ = "1.0.0"
__email__   = "sion.berg@elev.ga.dbgy.se"
'''

import os
import random
from colors import bcolors 

random.randint(1,100)
tries = 7

print(f"{bcolors.YELLOW}Välkommen till gissa talet!")
print(f"{bcolors.YELLOW}Du har 7 försök på dig!")
secret_number = random.randint(1,100)

while tries > 0:
    
    print(f"{bcolors.DEFAULT}Vad tror du det hemliga talet kan vara?" )
   
    try:
        guess = int(input())
    except:
        print(f"{bcolors.YELLOW}Du måste skriva siffor!")
        continue
    if guess < 1 or guess > 100:
        print(f"{bcolors.YELLOW}Talet är mellan 1-100!")
        continue

    if guess == secret_number:
        print(f"{bcolors.GREEN}Grattis! Du hittade det hemliga talet",secret_number,"med",tries-1,"försök kvar!.")
        print("Vill du fortsätta att spela? Svara Y/N: ")
        continue_playing = input()

        while True:
            
            if continue_playing == "Y" or continue_playing == "y":
                tries = 7
                secret_number = random.randint(1,100)
                break
            elif continue_playing == "N" or continue_playing == "n":
                print(f"{bcolors.RED}Avslutar")
                exit()
            else:
                print("Bara Y/N godkänns.")
            
    elif guess < secret_number:
        tries -=1
        print(f"{bcolors.RED}För lågt!")
        print(f"{bcolors.YELLOW}Du har",tries,"försök kvar!.")
    else:
        tries -=1
        print(f"{bcolors.RED}För högt!")
        print(f"{bcolors.YELLOW}Du har",tries,"försök kvar!.")
    if tries == 0:
        print(f"{bcolors.RED}Du lyckades inte att hitta det hemliga talet!")
        while True:
            print(f"{bcolors.GREEN}Vill du fortsätta att spela? Svara Y/N: ")
            continue_playing = input()
            if continue_playing == "Y" or continue_playing == "y":
                tries = 7
                secret_number = random.randint(1,100)
                break
            elif continue_playing == "N" or continue_playing == "n":
                print(f"{bcolors.RED}Avslutar")
                break
            else:
                print(f"{bcolors.YELLOW}Bara Y/N godkänns.")
                continue