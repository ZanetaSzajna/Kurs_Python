def fibonacci_iter(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    previous, next_word = 0, 1
    for i in range(n - 1):
        previous, next_word  = next_word , previous + next_word
    return next_word

