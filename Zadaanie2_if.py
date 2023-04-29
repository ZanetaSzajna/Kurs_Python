"""
Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, 
wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
"""

num1=int(input("Enter first number--> "))
num2=int(input("enter second number--> "))

sum=num2+num1

if sum>100:
    print("The sum of your numbers is equal: ", sum)
else:
    print("Koniec")