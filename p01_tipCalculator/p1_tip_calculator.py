# start here
print("Welcome to the tip Calculator!")
bill = int(input("What was the total bill? $"))
tipPercent = int(input("How much tip would you like to give? 10, 12, or 15? "))
totalPep = int(input("How many people to split the bill? "))
totalBill = bill * (1+tipPercent/100)
pay = totalBill / totalPep
personPay = round(totalBill / totalPep, 2)
print(f"Each person should pay: ${personPay}")