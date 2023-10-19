# memoization

def fib_memoization(n, cache=None):
    if cache is None:
        cache = {}
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]  # when the programme hit : return: the function will stop and complete from line 8

    cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)

    return cache[n]


print(fib_memoization(7))
# 0, 1, 1, 2, 3, 5, 8
