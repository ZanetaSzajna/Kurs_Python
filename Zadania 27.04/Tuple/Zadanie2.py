"""
Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
"""
Tuples = ("Apple", "Orange","Grape", "Watermelon", "Apple", "Orange" )
Lenght=len(Tuples)

for i in Tuples:
    con=Tuples.count(i)
    if con >1:
        print(i)