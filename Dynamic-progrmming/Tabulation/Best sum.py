def best_sum(target, numbers):  # time: O(m square n), space: O(m square)
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                combination = [*table[i], num]
                if i + num <= target:
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination

    return table[target]


print(best_sum(7, [5, 3, 4]))
print(best_sum(8, [5, 3, 2]))
print(best_sum(8, [5, 4, 1]))
print(best_sum(300, [7, 14]))
print(best_sum(300, [5, 1, 2, 25]))
print(best_sum(8, [2, 3]))

