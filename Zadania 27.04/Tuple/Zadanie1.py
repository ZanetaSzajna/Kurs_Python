"""
Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.
"""

animal = ('Cat','British cat','Mecenas')

for i in animal:
    print(i)

print(f" My pet is a {animal[0]}. His breed is {animal[1]}. His name is {animal[-1]}")