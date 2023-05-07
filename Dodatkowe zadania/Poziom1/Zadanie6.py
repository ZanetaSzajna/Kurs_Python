"""
Napisz program do odwrócenia ciągu znaków podanego przez użytkownika (np. "hello" powinno być wyświetlone jako "olleh").
Za pomocą string slicing
Za pomocą pętli for
Za pomocą pętli while
"""

print("String slicing ")
word = input("Enter word--> ")
print(word[::-1])

print("-----------------------------------------------------------------------------------------")
print("Loop FOR ")
lenght=len(word)
new_word=[]
for letter in range(0,lenght):
    new_word.append(word[lenght-1-letter])
print(''.join(new_word))
print("--------------------------------------------------------------------------------------------")
print("Loop WHILE")
character=0
n_word=[]
while character < lenght:
    n_word.append(word[lenght-1-character])
    character = character+1
print("".join(n_word))
