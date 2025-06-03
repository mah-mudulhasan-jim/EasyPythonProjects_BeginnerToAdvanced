import random
import string

print("Welcome to the PyPassword Generator")
print("The password must be AT LEAST 8 characters long and 32 characters long AT MOST")

def passGenerator1(nLetter,nNum, nSym):
  letters = list(string.ascii_lowercase)
  numbers = list(range(10))
  symbols = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
  tot = nLetter + nNum + nSym
  password = ""
  letCount = 0
  numCount = 0
  symCount = 0

  while len(password) < tot:
    pointList = random.randint(0, 2)
    if pointList == 0:
      if letCount < nLetter:
        password += random.choice(letters)
        letCount += 1
    elif pointList == 1:
      if numCount < nNum:
        password += str(random.choice(numbers))
        numCount += 1
    else:
      if symCount < nSym:
        password += random.choice(symbols)
        symCount += 1

  print(len(password))
  return password


def passGenerator2(nLetter, nNum, nSym): # More efficient
    letters = list(string.ascii_lowercase)
    numbers = list("0123456789")
    symbols = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    password_chars = []

    password_chars += random.choices(letters, k=nLetter)
    password_chars += random.choices(numbers, k=nNum)
    password_chars += random.choices(symbols, k=nSym)

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    print(len(password))
    return password

nLetter = int(input("How many letters would you like in yours password? "))

if nLetter > 32:
  print("The password length exceeds!!")
else:
  nNum = int(input(f"How many numbers? you have only {32 - nLetter} characters left. "))
  if nNum + nLetter > 32:
    print("The password length exceeds!!")
  else:
    nSym = int(input(f"How many Symbols? you have {32 - nLetter - nNum} characters left. "))
    if nSym + nNum + nLetter > 32:
      print("The password length exceeds!!")
    elif nSym + nLetter + nNum < 8:
      print("The password length is too short!!")
    else:
      password1 = passGenerator1(nLetter, nNum, nSym)
      print("Password 1: ",password1)
      password2 = passGenerator2(nLetter, nNum, nSym)
      print("Password 2: ",password2)