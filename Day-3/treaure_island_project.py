"""# Treasure Island Game

A beginner Python text adventure game.

## Features
- Door choices
- Water survival decision
- Mystery buildings
- ASCII art
"""


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# to print multiple lines use ''' ''' in print() instead of "".

print('''    ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|''')
print("you find yourself in a room with two doors, but you can oonly choose one ")
which_door = input(" CHOOSE THE DOOR ( RED OR BLUE)\n").lower()
if which_door == "red": # IF STRING VALUE THEN USE "" IN IF ELSE...
    print("YOU GOT LUCKY . NOW YOU FIND YOURSELF IN A DARK VALLEY SURROUNDED WITH WATER")
    print('''              ___
               /`  _\
               |  / 0|--.
          -   / \_|0`/ /.`'._/)
      - ~ -^_| /-_~ ^- ~_` - -~ _
      -  ~  -| |   - ~ -  ~  -
     jgs     \ \, ~   -   ~
              \_|''')
    swim = input("SWIM OR NOT (type yes or no) \n").lower()
    if swim == "yes":
        print("YOU ARE REALLY LUCKY.\n NOW YOU FIN YOURSELF IN FRONT OF 3 BUILDINGS BUT ONLY ONE IS SAFE.")
        building = int(input("ENTER BUILDING NO..... (type either 1 or 2 or 3.)\n")) # input always returns string so use int for integer..
        if building == 1:
            print("BURNED BY FIRE . GAME OVER")
        elif building == 2:
            print("AMBUSHED BY BEASTS...... GAME OVER....................")
        elif building == 3:
            print('''           ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')
            print(" YOU CHOOSE CORRECT......... YOU WIN ......... THE TREASURE IS YOURS.")
        else:
            print("ERROR ..... ONLY 3 BUILDINGS ........ MATRIX ERROR.......GAME OVER  ")
    else:
        print("YOU ARE AMBUSHED BY A GANG OF KILLERS .\n GAME OVER ")

else:
    print("GAME OVER . YOU ENTER A ROOM ON FIRE.")

