class Solution:

    @staticmethod
    def highest(arr):
        arr = sorted(arr)

        high_3 = arr[-1] * arr[-2] * arr[-3]
        lower_2_high_1 = arr[0] * arr[1] * arr[-1]

        return max(high_3, lower_2_high_1)


numbers = [1, 2, 3, 4, 5]
numbers1 = [-5, -2, -1, 0, 0, 1, 1, 5]
s = Solution()

print(s.highest(numbers))
print(s.highest(numbers1))
