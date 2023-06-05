"""
Wyświetl 3 losowe cytaty
"""
import random
with open("quotes.txt") as plik:
    quotes = plik.readlines()
    for i in range(3):
        quote = random.choice(quotes)
        quote = str(quote)
        quote = quote.replace("-", "\n\t")
        print(quote)

