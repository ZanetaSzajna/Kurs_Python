"""
Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
"""
word = input("Enter word -> ")
word_lenght=len(word)
print(word_lenght)
contains_a=word.count("a")
print(contains_a)
if word_lenght >= 5 and contains_a > 0:
    print(word.replace("a","z"))
else:
    print(word)