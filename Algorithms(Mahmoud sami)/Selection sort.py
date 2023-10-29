def selection_sort(arr):  # O(n square)
    for i in range(len(arr)):
        min_index = find_min(arr, i)
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap

    return arr


def find_min(arr, start_search):
    min_value = arr[start_search]
    min_index = start_search

    for i in range(start_search, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    return min_index


nums = [18, 39, 56, 47, 83, 10, 3, 48]

nums1 = selection_sort(nums)
print(nums1)




