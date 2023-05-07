"""
Napisz program, który wypisze liczby od 1 do 100, ale:
jeśli liczba jest podzielna przez 3, zamiast niej wypisz "Fizz"
jeśli liczba jest podzielna przez 5, zamiast niej wypisz "Buzz"
jeśli liczba jest podzielna przez 3 i przez 5, zamiast niej wypisz "FizzBuzz"

"""
for i in range(0,101):
    if i % 3 == 0 and i % 5 ==0:
        i="FizzBuzz"
        print(i)
    elif i % 3==0:
        i ="Fizz"
        print(i)
    elif i % 5 == 0:
        i="Buzz"
        print(i)
    else:
        print(i)
