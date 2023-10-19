# memoization


def grid(n, m, cache=None):

    if cache is None:
        cache = {}
    key = n, m

    if key in cache:
        return cache[key]

    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0

    cache[key] = grid(n - 1, m, cache) + grid(n, m - 1, cache)

    return cache[key]


print(grid(2, 3))
print(grid(18, 18))