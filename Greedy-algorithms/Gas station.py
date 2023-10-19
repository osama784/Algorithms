def can_complete_circuit(gas, cost):
    n = len(gas)
    curr = start = 0

    for i, (g, c) in enumerate(zip(gas * 2, cost * 2)):
        if i == start + n:
            return start

        curr += g - c

        if curr < 0:
            start = i + 1
            curr = 0

    return -1


print(can_complete_circuit([3, 5, 2, 1, 7], [4, 2, 1, 9, 1]))