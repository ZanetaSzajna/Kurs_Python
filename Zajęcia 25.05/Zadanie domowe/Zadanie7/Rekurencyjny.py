def ciag_fibonacciego(n):
    if n == 0: return 0
    elif n == 1: return 1
    return ciag_fibonacciego(n-1) + ciag_fibonacciego(n-2)



