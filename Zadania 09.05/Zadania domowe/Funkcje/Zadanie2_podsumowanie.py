"""
 Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
"""

a = int(input("Enter first number --> "))
b = int(input("Enter first number --> "))
c = int(input("Enter first number --> "))

def minimum_of(a,b,c):
    if a <b <c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
print(f" Minimum of numbers {a},{b},{c} is {minimum_of(a,b,c)}")