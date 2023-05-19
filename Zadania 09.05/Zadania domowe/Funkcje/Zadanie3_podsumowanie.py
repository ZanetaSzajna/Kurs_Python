"""
Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).
"""

a = int(input("Enter first number --> "))
b = int(input("Enter first number --> "))
c = int(input("Enter first number --> "))

def maximum_of (a,b,c ):
    if a > b and a>c:
        return  a
    elif b>a and b>c:
        return b
    else:
        return c

print("Maximum of a, b,c is ", maximum_of(a,b,c))