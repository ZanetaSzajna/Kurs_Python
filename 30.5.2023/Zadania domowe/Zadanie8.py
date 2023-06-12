"""
Wybierz zadanie z wszystkich zadań kursowych,
które wg Ciebie jest twoim najbardziej imponującym kodem napisanym do tej pory.
 Popraw ten kod zgodnie z tym czego się do tej pory nauczyłeś.

"""

numbers= input("Enter numbers, separate space -->  ")
list_numbers=numbers.split()

def even_number(list_numbers):
    even=[]
    for number in list_numbers:
        try:
            if int(number) % 2 ==0:
                even.append(number)
            print(even)
        except ValueError as error:
            print(error)
even_number(list_numbers)