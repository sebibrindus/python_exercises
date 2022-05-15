def fibonacci(n: int) -> int:
    '''

    Return the n_th Fibonacci number, for positive n.

    :param n: input given fron keyboard, last number in range
    :return: last Fibonacci in range

    '''

    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
