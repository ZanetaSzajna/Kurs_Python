
#1.Czy 23 + 3 będzie się równać 15 + 12 ?
example1 = 23 + 3 == 15 + 12
print("Rozwiązanie zadania 1:", example1)

#2.Czy dzielenie 29 przez 7 bez reszty wynosi 5?

example2 = (29 // 7) == 5
print("Rozwiązanie zadania 2",example2)

#3.Czy 27 podzielone przez 8 daje resztę 3?

example3 = (27 % 8) == 3
print("Rozwiązanie zadania 3" ,example3)

#4.Wyświetl True, jeżeli liczba jest parzysta.
print("Example 4")
liczba = int(input("Podaj liczbę--> "))
print("Rozwiązanie zadania 4: ",liczba, "jest parzysta ", liczba % 2 == 0)

#4a .Wyświetl True, jeżeli liczba jest parzysta - pętla

print("Example 4a")

liczba_1=int(input("Podaj liczbę --> "))
if liczba_1 % 2==0:
    print(liczba_1, "Jest liczbą parystą")
else:
    print(liczba_1, "jest nieparzysta")

#5.Czy 43 - 13 będzie się równać 11 + 12 ?

example5=43-13==11+12
print("Rozwiązanie zadania 5", example5)

#6.Czy dzielenie 129 przez 17 bez reszty wynosi 3?

example6 = 129 // 17 == 3
print("Rozwiązanie zadania 6",example6)

#7.Czy 247 podzielone przez 5 daje resztę 2?

example7 = 247 % 5 == 2
print("Rozwiązanie zadania 7", example7)

""""
# Dodatkowe -Czy liczba 17 jest przysta 
"""
print(17 % 2 == 0)
