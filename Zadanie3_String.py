#Do zmiennej quote przypisz zdanie: Honesty is the first chapter in the book of wisdom.”, a następnie:
quote= "Honesty is the first chapter in the book of wisdom."
#Policz wszystkie znaki w napisie
dlugosc_wyrazu=int(len(quote))
print("Liczba znakow = ", dlugosc_wyrazu)
#Nie modyfikując zmiennej wyświetl słowo wisdom
tablica_quote=quote.split(" ")
len_tab=len(tablica_quote)
wyraz=tablica_quote[9]
len_wyraz=len(wyraz)
print(wyraz[:len_wyraz-1])
#Wyświetl tylko pierwszą połowę tekstu
polowa=tablica_quote[:len_tab//2]
print(' '.join(polowa))
#Wyświetl tylko kropkę
print(quote[dlugosc_wyrazu-1])
#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[dlugosc_wyrazu//2::3])
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])
#Wyświetl cały cytat odwrotnie
print(quote[::-1])
#Zamień wisdom na słowo friendship
print(quote.replace("wisdom","friendship"))
