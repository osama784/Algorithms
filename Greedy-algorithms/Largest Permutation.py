class Solution:

    @staticmethod
    def solve(A, B):
        i = 0
        _max = len(A)
        d = {x: y for y, x in enumerate(A)}

        while B and i < len(A):
            j = d[_max]
            if i == j:
                pass
            else:
                B -= 1
                A[i], A[j] = A[j], A[i]
                d[A[i]], d[A[j]] = d[A[j]], d[A[i]]

            i += 1
            _max -= 1

        return A


s = Solution()
print(s.solve([1, 2, 3, 4], 1))


# s2 : (Mine)


def largest(arr, num_swaps):
    a = 0
    while a != num_swaps:

        b = max(arr[a:])

        ind_max = arr.index(b)
        temp = arr[a]
        arr[a] = b
        arr[ind_max] = temp
        a += 1

    return arr


numbers = [3, 2, 4, 1, 5]
print(largest(numbers, 3))
