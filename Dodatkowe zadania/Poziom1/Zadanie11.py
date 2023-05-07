"""
Napisz program, który używa pętli while do wyświetlenia kolejnych liczb parzystych, aż do momentu, gdy ich suma przekroczy wartość 100.
"""

number =0
sum_even =0
while number< 100:
      number=number+2
      sum_even=number+sum_even
      if sum_even< 100:
            print(number)
            print("Sum akolejnych liczb parzystych ", sum_even)
      elif sum_even==100:
            break
      