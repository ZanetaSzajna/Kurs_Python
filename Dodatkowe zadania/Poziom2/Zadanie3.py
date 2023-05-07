"""
Napisz grę w Większa / Mniejsza, w której komputer losuje liczbę z przedziału 1-100,
 a gracz musi odgadnąć, czy kolejna wylosowana liczba będzie większa czy mniejsza.
 Po każdym strzale program powinien podawać wynik, czy gracz wygrał czy
"""
import  random
i=True
while i:
    i=i+1
    computer1=random.randrange(1,100)
    print("The next number will be greater or less than ", computer1, "?")
    gamer= input("--> ")
    computer2=random.randrange(1,100)
    if gamer=="greater" and computer2 > computer1:
         print("The drawn number is", computer2)
         print("Congratulations you won!!! the next number was greater than", computer1)
         print("Try ", i-1)
         break
    elif gamer == "less" and computer2<computer1:
        print("The drawn number is", computer2)
        print("Congratulations you won!!! the next number was less than", computer1)
        print("Try ", i-1)
        break
    elif gamer == "greater" and computer2< computer1:
         print("The drawn number is", computer2)
         print("Unfortunately you lost the next number was less than", computer1)
         print("Try ", i-1)
    elif gamer == "less" and computer2>computer1:
        print("The drawn number is", computer2)
        print("Unfortunately you lost the next number was grater than", computer1)
        print("Try ", i-1)
    else:
        print("The entered data is incorrect")



