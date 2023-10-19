class Solution:
    def bulbs(self, arr):
        cost = 0

        for num in arr:
            if cost % 2 == 0:
                num = num
            else:
                num = not num

            if num % 2 == 1:
                continue
            else:
                cost += 1
        return cost


s = Solution()
# print(s.bulbs([1, 0, 1]))

# s2: (Main)


numbers = [1, 0, 1, 1]
count = 0


def bulbs1(arr):
    global count
    if len(arr) != 0:
        for i in range(len(arr)):
            if arr[i] == 1:
                continue
            else:
                count += 1
                new = flip(arr[i + 1:])
                return bulbs1(new)

    return count


def flip(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0

    return arr


# print(bulbs1(numbers))

nums = [0, 1, 0, 1, 1, 0, 1]
print(bulbs1(nums))
print(s.bulbs(nums))

nums1 = [1, 1, 0, 0, 1, 1]
print(s.bulbs(nums1))











