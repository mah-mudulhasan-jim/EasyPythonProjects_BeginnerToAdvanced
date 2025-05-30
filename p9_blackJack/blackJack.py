from banner9 import banner
import random

def calculateSum(card):
    total = 0
    for i in card:
        if i == 'J' or i == 'Q' or i == 'K':
            total += 10
        elif i == 'A':
            if total < 11:
                total += 11
            else:
                total += 1
        else:
            total += i
    return total

def stand(computer_card, cards):
    if calculateSum(computer_card) == 21:
        return 21
    else:
        cflag = True
        while cflag:
            computer_card.append(random.choice(cards))
            if calculateSum(computer_card) >= 17:
                cflag = False
        return calculateSum(computer_card)

def hit(player_card, cards):
    player_card.append(random.choice(cards))
    return player_card


def playBlackJack():
    print(banner)
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    player_card = random.sample(cards, 2)
    # player_card = ['A', 6]
    computer_card = random.sample(cards, 2)
    print(f"    Your cards: {player_card}, current score: {calculateSum(player_card)}")
    print(f"    Computer's first card: {computer_card[0]}")
    if calculateSum(player_card) == 21:
        print("    You win! It's a BlackJack")
    else:
        player_turn = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_turn != 'y':
            comp_score = stand(computer_card, cards)
            if calculateSum(player_card) < comp_score <= 21:
                print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                print(f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                print("You LOSE")
            elif comp_score > 21:
                print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                print(f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                print("Opponent went over. You WIN")
            elif comp_score < calculateSum(player_card):
                print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                print(f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                print("You WIN")
        else:
            pl_flag = True
            while pl_flag:
                player_card = hit(player_card, cards)
                print(f"    Your cards: {player_card}, current score: {calculateSum(player_card)}")
                print(f"    Computer's first card: {computer_card[0]}")
                if calculateSum(player_card) > 21:
                    print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                    print(f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                    print("You went OVER. You LOSE")
                    break
                else:
                    player_turn = input("Type 'y' to get another card, type 'n' to pass: ")
                    if player_turn != 'y':
                        pl_flag = False
                        comp_score = stand(computer_card, cards)
                        if calculateSum(player_card) < comp_score <= 21:
                            print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                            print(
                                f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                            print("You LOSE")
                        elif comp_score > 21:
                            print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                            print(
                                f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                            print("Opponent went over. You WIN")
                        elif comp_score < calculateSum(player_card):
                            print(f"    Your final hand: {player_card}, final score: {calculateSum(player_card)}")
                            print(
                                f"    Computer's Final hand: {computer_card}, final score: {calculateSum(computer_card)}")
                            print("You WIN")
gameFlag = True
while gameFlag:
    user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user == 'y':
        print("\n" * 20)
        playBlackJack()
    else:
        gameFlag = False


