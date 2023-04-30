"""
Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’)
"""
text=input("Please enter text --> ")
print(text [0::2])

print("-----------------------------------------------------------------------")

Text = input("Please enter text -->" )
list_text=list(Text)
len_text=len(Text)
for i in list_text:
    i=Text[::2]
print(i)