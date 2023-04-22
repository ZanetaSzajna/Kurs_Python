"""
Stwórz dwie zmienne s1 i s2
przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
"""

s1="Niezwykłe"
s2="samochody"
lenght=len(s1)
print(lenght)
s3=s1[0:(lenght//2)]+s2+s1[lenght//2:lenght]
print("Połączone s1 i s2 to: ", s3)

