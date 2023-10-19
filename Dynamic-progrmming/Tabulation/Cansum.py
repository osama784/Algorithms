def can_sum(target, numbers):  # time: O(mn), space: O(m)  m : target, n: len(numbers)
    table = [False] * (target + 1)
    table[0] = True
    for i in range(target):
        if table[i] is True:
            try:
                for num in numbers:
                    table[i + num] = True
            except IndexError:
                pass
    return table[target]


print(can_sum(7, [3, 2]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 5, 3]))
print(can_sum(4, [3, 3, 3]))
print(can_sum(300, [7, 14]))