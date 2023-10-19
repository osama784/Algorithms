def solve(arr):  # sorted arr: O(n), unsorted : O(nlogn)  n : len(arr)
    arr.sort(key=lambda x: x[1])
    num = []
    for i in range(len(arr)):
        num.append(arr[i][0])
        num.append(arr[i][1])
    prev = num[1]
    count = 1
    for i in range(1, len(num)):
        if i % 2 == 0:
            if num[i] >= prev:
                count += 1
                prev = num[i + 1]
            else:
                pass
    return count


print(solve([(10, 20), (12, 25), (20, 30)]))
print(solve([(10, 20), (20, 30), (30, 40)]))
print(solve([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))

# arr = [(0, 6), (3, 4), (1, 2), (5, 9), (5, 7), (8, 9)]
# arr.sort(key=lambda x: x[1])
# num = []
#
# print(num)
