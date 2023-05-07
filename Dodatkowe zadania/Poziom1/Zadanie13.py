"""
Napisz program, który używa pętli while do odgadnięcia liczby wylosowanej przez komputer z zakresu od 1 do 100.
Program powinien umożliwiać użytkownikowi wprowadzenie próby odgadnięcia i wyświetlić odpowiedni komunikat,
czy liczba jest za duża, za mała czy poprawna.
"""
import random
computer=random.randint(1,100)
print(computer)

i =True
while i:
    user= (input("Enter number--> "))
    if user == "koniec":
        print("Game brak by user")
        break
    elif int(user) == computer:
        print("Congrat you WIN !!!! ")
        break
    elif int(user) < computer:
        print("Your number is smaller then computer number")
    elif int(user)> computer:
        print("Your number is grater then computer number")

    else:
        print("Out range")