def fib(x):  # O(2 to the power 2)

    if x <= 1:
        return x

    else:
        return fib(x - 1) + fib(x + 1)


print(fib(3))

# s2:


def fib1(x):  # O(n)
    if x <= 1:
        return x
    n1 = 0
    n2 = 1
    n3 = 0
    i = 2

    while i <= x:
        i += 1
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n3


print(fib1(4))

# Fib series = 0, 1, 1, 2, 3, 5, 8, 13...
