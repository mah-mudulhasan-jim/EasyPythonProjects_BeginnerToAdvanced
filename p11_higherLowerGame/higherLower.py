import random
from game_data import data
from banner11 import higher_lower, vs


def create_option():
    # print(higher_lower)
    compare_arr =  random.sample(data, 2)
    opt1 = compare_arr[0]
    opt2 = compare_arr[1]
    print(f"Compare A: {opt1['name']}, a {opt1['description']}, from {opt1['country']}")
    print(vs)
    print(f"Against B: {opt2['name']}, a {opt2['description']}, from {opt2['country']}")
    return opt1, opt2


def main():
    print(higher_lower)
    option1, option2 = create_option()
    flag = True
    score = 0
    while flag:
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a':
            if option1['follower_count'] > option2['follower_count']:
                score += 1
                print("\n" * 20)
                print(higher_lower)
                print(f"You're right! Current score: {score}")
                print()
                option1, option2 = create_option()
            else:
                print("\n" * 20)
                print(higher_lower)
                print(f"Sorry That's Wrong. Final score: {score}")
                flag = False
                # return
        elif choice == 'b':
            if option2['follower_count'] > option1['follower_count']:
                score += 1
                print("\n" * 20)
                print(higher_lower)
                print(f"You're right! Current score: {score}")
                print()
                option1, option2 = create_option()
            else:
                print("\n" * 20)
                print(higher_lower)
                print(f"Sorry That's Wrong. Final score: {score}")
                flag = False
                # return
        else:
            print("\n" * 20)
            print(higher_lower)
            print(f"Sorry That's Wrong. Final score: {score}")
            flag = False


main()