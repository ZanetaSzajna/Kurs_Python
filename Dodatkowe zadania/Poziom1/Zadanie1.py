"""
Napisz program, który pyta użytkownika o dwie liczby i wyświetla wynik ich mnożenia,
ale tylko wtedy, gdy obie liczby są dodatnie. W przeciwnym wypadku wyświetl komunikat ”Nie mnożę!”
"""
number1=int(input("Enter first number --> "))
number2=int(input("Enter second number --> "))

if  number1> 0 and number2 > 0:
    multiplication=number1*number2
    print(multiplication)
else:
    print("Nie mnoże !")