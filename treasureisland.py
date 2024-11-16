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
print("Where do you want to go first?")

cross_road = input("Left or Right?: ")

if cross_road == "Left":
    print("Great! You have reached the Lake.\nDo you want to wait for the boat or swim your away?")
    swim_wait = input("Swim or Wait?: ")
    if swim_wait == "Wait":
        print(
            "Great Choice!\nYou have boarded the boat and reached the Big Door!\nChoose which door you want to go through,")
        which_door = input("Red, Blue, or Yellow?: ")
        if which_door == "Yellow":
            print("YOU WON!!!")
        elif which_door == "Red":
            print("You were burned by Fire!!\nGAME OVER")
        elif which_door == "Blue":
            print("You were eaten by the beasts!!\nGAME OVER")
        else:
            print("WRONG CHOICE\nGAME OVER")
    else:
        print("Uh Oh!, Wrong step!\nYou have been attacked by trout..\nGAME OVER")

else:
    print("Uh Oh!, Wrong Choice, You have fallen into a hole..\nGAME OVER")

print("Thank you for playing Treasure Island!")

