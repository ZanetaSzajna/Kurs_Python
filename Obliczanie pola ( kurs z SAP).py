lenght=float(input("Podaj dlugosc szescianu "))
widht=float(input("Podaj szerokosc szescianu "))
hight=float(input("Podaj wysokość szcześcianu "))

volume=lenght*widht*hight
surface=2*(lenght*widht)+2*(lenght*hight)+2*(widht*hight)

print("pole szescianu wynosi", surface)
print("objętosc szescianu wynosi ", volume)