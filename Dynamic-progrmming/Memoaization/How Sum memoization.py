def how_sum(target, numbers):  # time: O(n ^ m * m), space: O(m)  m = target n = numbers length  (Brute force)
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        result = how_sum(remainder, numbers)
        if result is not None:
            return [*result, num]


print(how_sum(7, [5, 3, 2, 2]))

# memoization


def how_sum1(target, numbers, cache=None):  # time : O(n*m ^2),  space : O(m^2)
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        result = how_sum1(remainder, numbers, cache)
        if result is not None:
            cache[target] = [*result, num]
            return cache[target]

    cache[target] = None


print(how_sum1(300, [7, 14]))
print(how_sum1(7, [5, 3, 2, 2]))
print(how_sum1(300, [10]))

# when you do the print: the cache in every time will be stored and be used in the next print statement
