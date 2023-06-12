"""
Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

"""

list=[]
word=""
len_word=0
with open("pan_tadeusz.txt",encoding='1250') as fopen:
    words=str(fopen.readline())
