"""
Napisz program, który używa pętli for do wyświetlenia gwiazdek w następującym kształcie.
Liczba “pięter” powinna zależeć od liczby wprowadzonej przez użytkownika w zakresie od 4 do 10
"""
floors=int(input("How many floors schould be your tower --> "))

if  4<floors<=10:
    for i in range(floors+1):
        k="*"*i
        print(k,)
else:
    if floors<4:
        print("Your tower should have more than 4 floors")
    else:
        print("Your tower should be no more than 10")