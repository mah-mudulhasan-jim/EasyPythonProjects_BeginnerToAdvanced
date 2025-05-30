from banner9 import banner
import random

def calculateSum(card):
    sum = 0
    for i in card:
        if i == 'J' or i == 'Q' or i == 'K':
            sum += 10
        elif i == 'A':
            if sum < 11:
                sum += 11
            else:
                sum += 1
        else:
            sum += i
    return sum

def stand(computerCard, cards):
    if calculateSum(computerCard) == 21:
        return 21
    else:
        cflag = True
        while cflag:
            computerCard.append(random.choice(cards))
            if calculateSum(computerCard) >= 17:
                cflag = False
        return calculateSum(computerCard)

def hit(playerCard, cards):
    playerCard.append(random.choice(cards))
    return playerCard


def playBlackJack():
    print(banner)
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    playerCard = random.sample(cards, 2)
    # playerCard = ['A', 6]
    computerCard = random.sample(cards, 2)
    print(f"    Your cards: {playerCard}, current score: {calculateSum(playerCard)}")
    print(f"    Computer's first card: {computerCard[0]}")
    if calculateSum(playerCard) == 21:
        print("    You win! It's a BlackJack")
    else:
        playerTurn = input("Type 'y' to get another card, type 'n' to pass: ")
        if playerTurn != 'y':
            computerScore = stand(computerCard, cards)
            if computerScore > calculateSum(playerCard) and computerScore <= 21:
                print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                print(f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                print("You LOSE")
            elif computerScore > 21:
                print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                print(f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                print("Opponent went over. You WIN")
            elif computerScore < calculateSum(playerCard):
                print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                print(f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                print("You WIN")
        else:
            plFlag = True
            while plFlag:
                playerCard = hit(playerCard, cards)
                print(f"    Your cards: {playerCard}, current score: {calculateSum(playerCard)}")
                print(f"    Computer's first card: {computerCard[0]}")
                if calculateSum(playerCard) > 21:
                    print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                    print(f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                    print("You went OVER. You LOSE")
                    break
                else:
                    playerTurn = input("Type 'y' to get another card, type 'n' to pass: ")
                    if playerTurn != 'y':
                        plFlag = False
                        computerScore = stand(computerCard, cards)
                        if computerScore > calculateSum(playerCard) and computerScore <= 21:
                            print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                            print(
                                f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                            print("You LOSE")
                        elif computerScore > 21:
                            print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                            print(
                                f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                            print("Opponent went over. You WIN")
                        elif computerScore < calculateSum(playerCard):
                            print(f"    Your final hand: {playerCard}, final score: {calculateSum(playerCard)}")
                            print(
                                f"    Computer's Final hand: {computerCard}, final score: {calculateSum(computerCard)}")
                            print("You WIN")
gameFlag = True
while gameFlag:
    user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user == 'y':
        print("\n" * 20)
        playBlackJack()
    else:
        gameFlag = False


