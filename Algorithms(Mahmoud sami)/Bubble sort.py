def bubble_sort(arr):  # O(n square)
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):  # to not get out of the range cause j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        continue  # the most important line

    return nums


nums = [2, 4, 1, 5, 3, 6, 1]
nums1 = bubble_sort(nums)
print(nums1)