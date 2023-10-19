def grid_traveller(m, n):
    table = []
    for i in range(m + 1):
        table.append([0] * (n + 1))

    table[1][1] = 1
    for x in range(m + 1):
        for y in range(n + 1):
            current = table[x][y]
            if y + 1 <= n:
                table[x][y + 1] += current
            if x + 1 <= m:
                table[x + 1][y] += current

    return table[m][n]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
