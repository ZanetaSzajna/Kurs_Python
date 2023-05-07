"""
Napisz program, który używa pętli for do zamiany miejscami dwóch elementów tablicy o określonych przez użytkownika indeksach.
"""

lista=["ALa", 'ma ', "kota", "a", "kot", "ma", "Alę"]
print(lista)
i = int(input("podaj pierwszy indeks zamiany-->  "))
j= int(input("Podaj drugi indeks zamiany --> "))

for word in lista:
    if word == lista[i]:
        new_i = word
        lista[i] = lista[j]
        lista[j] = new_i
print(lista)