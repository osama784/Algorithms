# inefficient solution for big numbers:

def solve(seats):
    MOD = 10000003

    crosses = [i for i, c in enumerate(seats) if c == 'x']
    crosses = [(cross - i) for i, cross in enumerate(crosses)]

    n = len(crosses)
    if n == 0 :
        return 0

    ans = float('inf')
    for segment_start in range(len(seats)):  # O(n)
        total = 0
        for cross in crosses:  # O()n
            total += abs(cross - segment_start)
            total %= MOD
        ans = min(ans, total % MOD)

    return ans


print(solve('..xx..'))
print(solve('..x..x'))


def solve1(seats):
    MOD = 10000003

    crosses = [i for i, c in enumerate(seats) if c == 'x']  # indices of x(s)
    crosses = [(cross - i) for i, cross in enumerate(crosses)]  # the crosses between the x(s)

    n = len(crosses)
    if n == 0:
        return 0

    ans = float('inf')  # infinity

    segment_start = crosses[n // 2]
    total = 0
    for cross in crosses:
        total += abs(cross - segment_start)
        total %= MOD
    ans = min(ans, total % MOD)

    return ans


print(solve1('..x..x..x'))
