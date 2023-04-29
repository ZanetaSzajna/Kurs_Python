"""
Sortowanie.
Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
"""
number1 = int(input("Enter first number--> "))
number2 = int(input("Enter second number--> "))
number3 = int(input("Enter third number--> "))
maximum=max(number1,number2,number3)

print("Before sorting: ", number1, number2, number3)
print("The biggest number", maximum)

if number1 < number2 < number3:
    print("After sorting" ,number1 , number2,number3)
elif number1<number3 <number2:
    print("After sorting: ", number1, number3, number2)
elif number2 < number1 < number3:
    print("After sorting: ",number2, number1, number3)
elif number2 < number3 < number1:
    print("After sorting: ",number2,number3,number1)
elif number3 < number1 < number2:
    print("After sorting: ",number3,number1,number2)
else:
    print("After sorting: ",number3,number2,number3)


