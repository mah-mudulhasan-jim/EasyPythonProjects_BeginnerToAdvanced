def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 -  n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
# calDict = {
#         '+': add,
#         '-': substract,
#         '*': multiply,
#         '/': divide
#         }
def calculate():
    from banner8 import banner
    print(banner)
    calDict = {
        '+': add,
        '-': substract,
        '*': multiply,
        '/': divide
    }
    num1 = float(input("What's the first number?: "))
    # flag = True
    while True:
        ops_arr = []
        for ops in calDict:
            ops_arr.append(ops)
            print(ops)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        if operation not in ops_arr:
            print(f"{num1} undefined {num2} = 0.0")
            val = 0
        else:
            val = calDict[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {val}")
        choice = input("Type 'y' to continue calculating with 18.0, or type 'n' to start a new calculation: ")
        if choice == 'y':
            num1 = val
        else:
            # flag = False
            print("\n" * 100)
            calculate()

calculate()