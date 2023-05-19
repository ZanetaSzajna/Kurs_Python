"""
Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
"""
import random

lower = int(input("Enter lower limit of the range --> "))
upper= int(input("Enter upper limit of range -> "))

random_number = random.randint(0,100)
print(random_number)

def is_in_user_range(lower, upper, random_number):
    if random_number  in range(lower, upper):
        print( f"Number {random_number} is in  range ({lower}, {upper+1}) ")
    else:
        print(  f"Number {random_number} is not in range ({lower}, {upper+1})")

is_in_user_range(lower, upper,random_number)