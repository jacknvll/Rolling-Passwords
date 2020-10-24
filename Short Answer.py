from random import choice
from Dice import Die_D4, Die_D8, Die_D10, Die_D16, Die_D30
Password, UpperLimit = [], choice(Die_D4) + choice(Die_D4) + 10
while len(Password) <= UpperLimit:
    InitialRoll = choice(Die_D4)
    if InitialRoll == 1:
        Password.append(str(choice(Die_D8))) if choice(Die_D30) == '-' else Password.append(str(choice(Die_D30)))
    if InitialRoll == 2:
        Password.append(str(choice(Die_D8))) if choice(Die_D30) == '-' else Password.append(str(choice(Die_D30).upper()))
    Password.append(choice(Die_D10)) if InitialRoll == 3 else Password.append(choice(Die_D16))
print("The char count is: ", UpperLimit, "\nThe rolling password is: ", "".join(Password))