"""
Wyświetl tylko 5 pierwszych linii

"""

with open("pan_tadeusz.txt",encoding='1250') as fopen:
   for i in range(5):
      content=fopen.readline()
      print(content)