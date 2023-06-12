
# Wywołaj błąd związany z otwarciem pliku.
# Spróbuj odczytać plik, który nie istnieje.

with open("klasa" ) as fopen:
    try:
        fopen.read()
    except (FileNotFoundError) as mistake:
        print(" Sorry, we cannot find the file you are trying to open, please check the file name ")
import io

#Spróbuj odczytać wartość z pliku otwartym w trybie w

with open("notes.txt", "w") as fopen:
    try:
        poem=fopen.readlines()
        print(poem)
    except io.UnsupportedOperation as error:
        print(error)

#Spróbuj utworzyć plik, który już istnieje w trybie x
try:
    with open("exist.txt","x") as fopen:
        fopen.write("klasa")
except FileExistsError as err:
        print(err)




