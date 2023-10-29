# s1:
nums = [4, 9, 3, 6, 2]

for i in range(len(nums)):
    min_idx = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums)

# s2:


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


selection_sort(nums)
print(nums)


