"""
Napisz program, który wyświetla liczbę wyrazów w podanym przez użytkownika ciągu znaków (zakładamy, że wyrazy dzielą się spacją).
"""

sentence = input("Enter a sentence separate space --> ")
sentence = sentence.split()
list_sentence = list(sentence)
words=len(list_sentence)
print("Your sentence have ", words, "words")