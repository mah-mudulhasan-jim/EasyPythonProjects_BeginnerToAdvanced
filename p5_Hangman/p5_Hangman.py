from HangManWords import words
import random
from helpingFunction import arr_to_str, str_to_arr
from stages import stage

chosenWord = random.choice(words)
# print(chosenWord)
guessed_word = ""
for _ in range(len(chosenWord)):
    guessed_word += "_"
win = False
life = 6
temp = life
count = 0
stage_index = 0
input_arr = []
while life != 0 and not win:
    print(f"Word to Guess: {guessed_word}")
    user = input("Guess a letter: ").lower()
    if user not in input_arr:
        input_arr.append(user)
        print(1, input_arr)
        if len(user) != 1:
            print("Enter only 1 letter")
            print(stage[stage_index])
        elif user in chosenWord:
            idx_arr = []
            for i in range(len(chosenWord)):
                if chosenWord[i] == user:
                    idx_arr.append(i)
            temp_word = str_to_arr(guessed_word)
            for i in idx_arr:
                temp_word[i] = user
            guessed_word = arr_to_str(temp_word)
            print(guessed_word)
            print(stage[stage_index])
            print(f"****************************{life}/{temp} LIVES LEFT****************************")
            print()
            for i in guessed_word:
                if i != "_":
                    count += 1
            if count == len(guessed_word):
                win = True
                print("You won")
            else:
                count = 0
        else:
            stage_index += 1
            print(stage[stage_index])
            print(f"You chose {user}. That is not in the word. You lose a life")
            life -= 1
            if life != 0:
                print(f"****************************{life}/{temp} LIVES LEFT****************************")
                print()
    else:
        print("CAUTION: You have already guessed this letter")
        print(stage[stage_index])
        print(f"****************************{life}/{temp} LIVES LEFT****************************")
        print()
if life == 0:
    print(f'''You lost. The correct word is : {chosenWord}
****************************{life}/{temp} LIVES LEFT****************************''')