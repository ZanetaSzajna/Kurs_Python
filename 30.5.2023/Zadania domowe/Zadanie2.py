""""
Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
Pozwól użytkownikowi podać dowolny index oraz wartość.
Spróbuj w krotce podmienić wartość na zadanym indeksie.
Obsłuż błąd
"""

tup = (5,36,25,45,85,3,65,45,1,22)
index = int(input("Enter index --> "))
value = input("Enter a value --> ")


try:
    tup[index]= value
except TypeError as error:
    print("Przepraszamy nie możemy zmienić wartości  krotki ")