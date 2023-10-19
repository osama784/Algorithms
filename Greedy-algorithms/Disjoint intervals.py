class Solution:
    def solve(self, arr):
        arr.sort(key=lambda x: x[1])

        prev_start, prev_end = arr[0]
        count = 1
        set_arr = [arr[0]]  # my
        for start, end in arr:
            if start <= prev_end:
                pass
            else:
                prev_start, prev_end = start, end
                count += 1
                set_arr.append([prev_start, prev_end])  # my

        return count, set_arr


s = Solution()
numbers1 = [[1, 4], [2, 3], [4, 6], [8, 9]]
print(s.solve(numbers1))


# mine:

def disjoint(arr):
    arr.sort()
    set_arr = [arr[0]]
    for i in arr:
        for y in set_arr:
            if y[-1] == i[0] or y[-1] > i[0]:
                pass
            else:
                set_arr.append(i)
    return set_arr


numbers = [[2, 10], [4, 6], [1, 2]]
numbers1 = [[1, 4], [2, 3], [4, 6], [8, 9]]
print(disjoint(numbers))
print(disjoint(numbers1))












