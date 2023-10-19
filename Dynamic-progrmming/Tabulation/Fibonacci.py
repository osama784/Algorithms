def solve(n):  # O(n) time and space, both of the function
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, len(table)):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


print(solve(50))

# or:


def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(0, n):
        if i != n:
            table[i + 1] += table[i]
        if i != n - 1:
            table[i + 2] += table[i]

    return table[n]


print(fib(6))

# or :


def best(n):
    pre_prev = 0
    prev = 1
    track = 0
    for i in range(n - 1):
        track += pre_prev + prev
        pre_prev = prev
        prev = track
        track = 0
    return prev


print(best(7))
