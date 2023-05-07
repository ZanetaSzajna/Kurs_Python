"""
Napisz program, który używa pętli while do wyświetlenia kwadratów kolejnych liczb całkowitych,
począwszy od 1, aż do momentu, gdy wartość największego wyświetlonego kwadratu przekroczy wartość 100.
"""
num =0
sum_num=0

while  sum_num < 100:
    sum_num=(sum_num+1)**2
    print(sum_num)