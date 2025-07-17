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
choice_1 = input("you're cross the road.where do you want to go:?\ntype left or right").lower()
if choice_1 == "left":
    choice_2 = input('you\'ve come to a lake.There is an island in the lake,'
                     'Type "wait" for wait a boat or "swim" to swim accross the lake').lower()
    if choice_2 == "wait":
        choice_3 = input("you reached the river unharmed.There is three door infront of you."
                          "which door do you choose:?RED ,YELLOW, BLACK")

        if choice_3 == "red":
                         print("room has full of fire.Game over")
        elif choice_3 == "black":
                        print("it has most terrible room.Game over")
        elif choice_3 == "yellow":
                         print("it is golden room.you win")
    else:
        print("you got in trouble.GAME OVER!")

else:
    print("you got in trouble.GAME OVER!")
