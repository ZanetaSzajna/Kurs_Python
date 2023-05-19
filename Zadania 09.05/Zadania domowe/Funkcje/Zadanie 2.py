"""
Napisać funkcję, która sprawdza czy liczba jest parzysta.
"""

def even_number():
    number=int(input("Please enter number --> "))
    if number % 2 == 0:
        print(f'{number} is even ')
    else:
        print(f"{number} is odd")
even_number()