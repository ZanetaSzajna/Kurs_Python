n= int(input("Podaj liczbę "))

for i in range(n+1):
    if i % 3 == 0 and i% 5 ==0:
        print('FooBar')
    elif i% 3==0:
        print('Foo')
    elif i%5 == 0:
        print('Bar')
    else:
        print(i)
