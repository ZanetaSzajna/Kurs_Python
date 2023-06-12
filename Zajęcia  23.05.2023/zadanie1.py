"""
Utwórz plik zawierający listę ok. 20 cytatów.
Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.

zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora
"""


import random

def download_file():

    with open("quotes.txt") as plik:
        quotes=plik.readlines()
    return quotes



def show(quote):
    print("Quote od the day is :")
    print()
    width = 100
    print("*"*width)

    print(quote.strip().center(width))
    print("*"*width)

def main():
    quotes=download_file()
    quote = random.choice(quotes)
    quote=str(quote)
    quote=quote.replace("-", "\n\t" )
    show(quote)
    name_file = input("How want you save your file-->  ")
    with open(f"{name_file}.txt", 'w') as f:
        f.write(quote)

main()


