"""
Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

Dorota, Wellman, dziennikarka

Adam, Małysz, sportowiec

Robert, Lewandowski, piłkarz

Krystyna, Janda, aktorka

Wyświetl w sposób przyjazny dla użytkownika
"""
list=[
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]

print(list)

for person in range(len(list)):
   for i in range(len(list[person])):
        print(list[person][i], end=' ')
   print()