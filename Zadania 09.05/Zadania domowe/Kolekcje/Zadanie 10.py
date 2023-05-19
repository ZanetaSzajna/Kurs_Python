"""
Użytkownik podaje dowolną liczbę N.
Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
"""
square_number ={}
N = int(input(" Enter a number --> "))

for number in range(1,N+1):
    square_number[number]=number*number
print(square_number)