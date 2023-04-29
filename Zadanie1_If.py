"""
Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
"""
num=int(input("Enter a number --> "))
if num % 3 ==0:
    print("Number", num, " is divisible by 3")
else:
    print("Number", num, "isn't divisible by 3")