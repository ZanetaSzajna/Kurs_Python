"""
Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”
"""
items = str(input("What will you take on a solo trip?--> "))
lista = items.split()

for i in lista:
    i = i.strip(",")
    print(i)

print("Great, we are ready!")