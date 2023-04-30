"""
 W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
"""
text = str(input("Please enter text --> "))
list_text=list(text)
lower=[]
up=[]
digit=[]
white_sign=[]
for i in list_text:
    if i.islower()==True:
        lower.append(i)
    elif i.isdigit()==True:
        digit.append(i)
    elif i.isupper()==True:
        up.append(i)
    elif i.isspace()==True:
        white_sign.append(i)
print("The number of lowercase letters in your text is:", len(lower))
print("The number of capital letters in your text is: ", len(up))
print("The number of digits in your text is:", len(digit))
print("The number of whitespace characters in your text is:", len(white_sign))