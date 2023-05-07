"""
Napisz program, który wyświetla sumę wszystkich liczb parzystych z zakresu od 1 do 100.
Dodaj przy liczbie wykrzyknik tylko wtedy, gdy liczba jest podzielna przez 3.
"""
suma=0
for i in range(1,101):
    if i % 2 == 0:
        suma=suma+i
        if suma % 3 == 0:
            print( suma,"!!!!")
        else:
            print(suma)

