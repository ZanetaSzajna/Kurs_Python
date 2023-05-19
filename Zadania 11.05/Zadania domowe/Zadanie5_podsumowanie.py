"""
Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

"""

import random

def warm_cold(comp, user,round):
    if comp == user:
        print("Congrat, YOU WIN !!!!!!!!!!!!!!!!")
    elif 0 < user_nuber < computer and i < int(round):
        print("Warm")
    elif computer < user_nuber < 100 and i < int(round):
        print("Cold")

computer = random.randrange(0, 101)
round=int(input("How many round you want play >"))


for i in range(0,round):
    user_nuber = int(input("select a number from 0 to 100 -->  "))
    print(warm_cold(computer, user_nuber, round))
if computer == round:
    print("You win")
else:
    print("Sorry you lose computer chosse number: ",computer)