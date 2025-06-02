from menu import MENU, RESOURCE
from banner12 import banner


def is_resource_suffice(resource, item):
    # print(item["ingredients"])
    # print('bug: ', resource)
    for ingredient in item["ingredients"]:
        # print(ingredient)
        # print(item["ingredients"][ingredient])
        if item["ingredients"][ingredient] > resource[ingredient]:
            return f'Sorry, There is not enough {ingredient}'
    for ingredient in item['ingredients']:
        resource[ingredient] -= item["ingredients"][ingredient]
    return True


def main():
    print(banner)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        return
    elif user_choice == 'report':
        print(f'''
        Current Resource:
        Water: {RESOURCE['water']}ml
        Milk: {RESOURCE['milk']}ml
        Coffee: {RESOURCE['coffee']}g
        Money: ${RESOURCE['Money']}    
    ''')
    else:
        if  is_resource_suffice(RESOURCE, MENU[user_choice]) != True:
            print(is_resource_suffice(RESOURCE, MENU[user_choice]))
        else:
            print("Please insert coins.")
            arr = ['quarters', 'dimes', 'nickles', 'pennies']
            values = {
                'quarters': 0.25,
                'dimes': 0.10,
                'nickles': 0.05,
                'pennies': 0.01
            }
            price = sum(int(input(f"How many {i}?: ")) * values[i] for i in arr)
            if price > MENU[user_choice]['cost']:
                print(f"Here is ${price - MENU[user_choice]['cost']} in change")
                RESOURCE['Money'] += MENU[user_choice]['cost']
                print(f"Here is your {user_choice} ☕ Enjoy!")
            elif price < MENU[user_choice]['cost']:
                print("Sorry that's not enough money. Money Refunded")
    print()
    # print("\n"*20)
    main()


main()

