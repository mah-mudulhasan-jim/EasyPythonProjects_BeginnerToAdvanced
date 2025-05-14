print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print('''Welcome to Treasure Island!
Your mission is to find the TREASURE''')
print("Now you are at a point of a dangerous jungle filled with animals, rivers and what not!. You have 2 ways to go. Right or left. which one do you choose? ")
choice1 = input().lower()
if choice1 != 'left':
    print("You fell into a hole. GAME OVER Dude!")
else:
    print("To your utter Surprise, after walking you found a river. But there is no Boat!! How can you pass the river then? Well. You can either wait for a boat or you can swim. What are you gonna do Buddy? 'wait' or 'swim??'")
    choice2 = input().lower()
    if choice2 != 'wait':
        print("Oops!!! You were attacked by trout! GAME OVER!! Better luck next time")
    else:
        print("You got a boat after waiting and crossed the river. What a luck!")
        print("Now you are in front of 3 house. You have to choose the right door. There are 3 colors on the doors. 'Red', 'Yellow' and 'Blue'")
        choice3 = input("So now choose one color. 1. 'Red', 2. 'Blue' 3. 'Yellow'").lower()
        if choice3 == 'red':
            print("Dude is burned by fire!!")
            print("GAME OVER!!")
        elif choice3 == 'blue':
            print("Got eaten by beasts!")
            print("GAME OVER!!")
        elif choice3 == 'yellow':
            print("Damn Bro!! You got it! You found the treasure")
            print("Congratulations!! You won!!!")
        else:
            print("Wrong move at the end! BAD LUCK")
            print("GAME OVER!")

