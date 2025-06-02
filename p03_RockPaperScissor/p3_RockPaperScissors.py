import random

print("Welcome to ROCK - PAPER - SCISSORS")
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Enter your turn. (0 for Rock, 1 for paper, 2 for scissor)")
userTurn = int(input())
print("Your choice:")
if userTurn == 0:
    print("rock")
    print(rock)
elif userTurn == 1:
    print("paper")
    print(paper)
elif userTurn == 2:
    print("scissor")
    print(scissor)
compTurn = random.randint(0, 2)
print("Computer's choice:")
if compTurn == 0:
    print("rock")
    print(rock)
elif compTurn == 1:
    print("paper")
    print(paper)
elif compTurn == 2:
    print("scissor")
    print(scissor)

if compTurn == userTurn:
    print("It's a TIE")
else:
    if compTurn == 0:
        if userTurn == 1:
            print("You win!")
        elif userTurn == 2:
            print("Computer wins!")
    elif compTurn == 1:
        if userTurn == 0:
            print("Computer wins!")
        elif userTurn == 2:
            print("You win!")
    elif compTurn == 2:
        if userTurn == 1:
            print("Computer wins!")
        elif userTurn == 0:
            print("You wins")