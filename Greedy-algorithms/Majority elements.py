# Naive solution: time and space: O(N)
from collections import Counter


def solve(arr):
    return Counter(arr).most_common()[0][0]


print(solve([4, 2, 2, 3, 2, 2]))


# Sneaky solution: time : O(log(w).N) , space: O(1)

def solve_(nums):
    n = len(nums)
    ans = 0
    for b in range(32):
        ones = 0
        for num in nums:
            if (1 << b) & num:  # 1 << (number) means: 2 to the power number
                ones += 1
        if ones > (n // 2):
            ans += 1 << b

    return ans

print(solve_([4, 2, 2, 3, 2, 2]))
