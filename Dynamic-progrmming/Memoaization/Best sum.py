def best_sum(target, numbers, cache=None):
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        remainder_combination = best_sum(remainder, numbers, cache)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    cache[target] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(100, [1, 2, 5, 25]))
print(best_sum(300, [10]))

# the same as how sum
