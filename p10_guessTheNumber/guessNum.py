import random
from banner10 import banner
def guess_number(num):
    guess = int(input("Make a guess: "))
    if  guess == num:
        print(f"That's correct. The number was {guess}")
        return True
    elif guess > num:
        print(f'''
                Too HIGH
                Guess again
                ''')
        return False
    else:
        print(f'''
                Too LOW 
                Guess again
        ''')
        return False


def main():
    print(banner)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty != 'easy':
        turn = 5
    else:
        turn = 10
    remain = turn
    for _ in range(turn):
        print(f"You have {remain} attempts remaining to guess the number.")
        result = guess_number(number)
        if result:
            return
        else:
            remain -= 1
    print("You've run out of guesses. Refresh the page to run again.")
    return

if __name__ == "__main__":
    main()