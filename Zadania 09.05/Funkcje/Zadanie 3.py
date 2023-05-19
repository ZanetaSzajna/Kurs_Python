"""
Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
"""

numbers= input("Enter numbers, separate space -->  ")
list_numbers=numbers.split()

def sum_number():
    sum_num=0
    for number in list_numbers:
        sum_num += int(number)
    print(sum_num)

sum_number()