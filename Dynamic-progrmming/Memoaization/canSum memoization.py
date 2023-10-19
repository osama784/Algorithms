def can_sum(target, numbers, cache=None):
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        reminder = target - num
        if can_sum(reminder, numbers, cache):  # == True
            cache[target] = True
            return True

    cache[target] = False
    return False


print(can_sum(7, [5, 3, 4]))
print(can_sum(300, [7, 14]))