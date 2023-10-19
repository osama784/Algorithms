def how_sum(target, numbers):  # time O(m square *n)  space: O(m square)
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            try:
                for num in numbers:
                    table[i + num] = [*table[i], num]  # copying
            except IndexError:
                pass
    return table[target]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [7, 14]))
