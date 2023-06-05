from Rekurencyjny import ciag_fibonacciego
from Iteracyjny import fibonacci_iter

n= int(input("Enter number -- > "))

fibonacci_rek= ciag_fibonacciego(n)
fibonacci_iter=fibonacci_iter(n)

print("Rekurencyjny ")
print(f"The {n}th expression of the Fibonacci sequence is equal to {fibonacci_rek} ")

print("Iteracyjny")
print(f"The {n}th expression of the Fibonacci sequence is equal to {fibonacci_iter} ")
