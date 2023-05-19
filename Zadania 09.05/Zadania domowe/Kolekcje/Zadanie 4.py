"""
Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.
"""

for row in range (1, 11):
    for col in range(1,11):
        print( row * col, end=" \t")
    print()

    