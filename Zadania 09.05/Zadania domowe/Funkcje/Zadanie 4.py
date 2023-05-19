"""
Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
"""
numbers= input("Enter numbers, separate space -->  ")
list_numbers=numbers.split()

def even_number(list_numbers):
    even=[]
    for number in list_numbers:
        if int(number) % 2 ==0:
            even.append(number)
    print(even)

even_number(list_numbers)