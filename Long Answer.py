#Pre-Requisites
from random import choice
from Dice import Die_D4, Die_D8, Die_D10, Die_D16, Die_D30

# Variable
Password = []

# UpperLimit
UpperLimit = choice(Die_D4) + choice(Die_D4) + 10
print("The char count is: ", UpperLimit)

# DEFINITIONS:
def option1():
    tmp = choice(Die_D30)
    Password.append(choice(Die_D8)) if tmp == '-' else Password.append(tmp)

def option2():
    tmp = choice(Die_D30)
    Password.append(choice(Die_D8)) if tmp == '-' else Password.append(tmp.upper())

def option3():
    tmp = str(choice(Die_D10))
    Password.append(tmp)

def option4():
    tmp = choice(Die_D16)
    Password.append(tmp)

# Switch Statement
while len(Password) <= UpperLimit:
    InitialRoll = choice(Die_D4)
    if InitialRoll == 1:
        option1()
    if InitialRoll == 2:
        option2()
    if InitialRoll == 3:
        option3()
    if InitialRoll == 4:
        option4()

# Final
print("The rolling password is: ", "".join(Password))