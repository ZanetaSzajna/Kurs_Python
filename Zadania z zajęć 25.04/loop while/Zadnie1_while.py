"""
Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
"""
F=0
while 0 <= F < 200:

    F=F+20
    C=(5/9) *(F-32)
    print(F,"F --> ",round(C,2),"C")

print("-----------------------------------------------------------")

print("Use loop for")
f=0
for f in range(0, 201,20):
    c=(5/9)*(f-32)
    print(f, "F--> ", round(c,2),"C")