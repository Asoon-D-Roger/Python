print ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
choice1 =input ("Here are the two directions in frent of you. So which directions do you want to take (Left or right).").lower()
if choice1 == "left":
    choice2=input("Well done you reached to the crosslake. Type wait for the boat . type swim  across").lower()
    if choice2 == "wait":
        choice3 = input("you arrived to the island unharmes. There is a house with three doors. one red , one yellow, one blue.So which color do you want to choose?").lower()
        if choice3 == "red":
            print("It is a room with full of snakes and you have died due to beatern by snakes. Game over. ")
        elif choice3 == "yellow":
            print("Hurrey. you finded the treasure and you won the game.")
        elif choice3 == "blue":
            print("You reachde into the room of fire and and you stucked in the fire . game over.")
        else:
            print("you reached the place where dosen't exist . Game over.")    
else:
    print("Sorry, you fell into the hole . Game over.")

