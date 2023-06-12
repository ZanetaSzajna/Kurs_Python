"""
 Oblicz średnią arymetyczną z kilku liczb.
 Liczby będą podane przez użytkownika po przecinku.
 Napisz funkcję, która przyjmie wartości i wyświetli średnią.
 Program powinen być odporny na błędy użytkownika.
 Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
"""
numbers = input("Please enter a number separate a space --> ")
numbers=numbers.split()
list_of_numbers = list(numbers)

lenght = len(list_of_numbers)


def sum_number(list_of_numbers):
    sum_numbers =0
    for number in list_of_numbers:
        try:
            sum_numbers += int(number)

        except ValueError as error:
            error=str(error)
            with open("Errors", "a") as fopen:
                fopen.write(error)
    return sum_numbers

sum_numbers = sum_number(list_of_numbers)
def average(sum_numbers):
    try:
        average = sum_numbers/lenght
        return average
    except TypeError as terror:
        terror = str(terror)
        with open("Errors","a") as file:
            file.write(terror)

average(sum_numbers)

print(f"the average of the numbers {list_of_numbers} is equal {average(sum_numbers)}")
