from banner7 import banner


def secretAuction(dict):
    max = 0
    maxPlayer = ''
    for key in dict.keys():
        if dict[key] > max:
            max = dict[key]
            maxPlayer = key
    print(f"The winner is {maxPlayer} with a bid of ${max}")


def main():
    playerAvailable = True
    auctionDict = {}
    print(banner)
    while playerAvailable:
        player = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        auctionDict[player] = bid
        availableCheck = input("Are there any other bidders? Type 'yes or 'no'.").lower()
        if availableCheck == 'no':
            playerAvailable = False
        elif availableCheck == 'yes':
            print("\n" * 100)
        else:
            print("You should type 'yes' or 'no'")
            availableCheck = input("Are there any other bidders? Type 'yes or 'no'.").lower()
            if availableCheck == 'yes':
                print("\n" * 100)
    secretAuction(auctionDict)


if __name__ == "__main__":
    main()