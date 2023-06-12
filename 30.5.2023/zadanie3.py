lista=[1.6, 7,8,9,'koniec', 'pamięć',20]
user_index=input("Podaj indeks który chcesz wyświetlić --> ")

try:
    x=lista[int(user_index)]
    print(x)
except (TypeError, ValueError, IndexError) as error :
    print( error)
