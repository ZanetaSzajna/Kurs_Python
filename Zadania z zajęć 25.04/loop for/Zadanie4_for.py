"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
"""
N =int(input("Enter number <= 8 --> "))

if N<= 8 and N>0:
    silnia =1
    for i in range(2,N+1):
        silnia=silnia*i
    print("Silnia z ",i,"wynosi", silnia)
else:
    print("I can't calculate becouse you enter number greater than 8")