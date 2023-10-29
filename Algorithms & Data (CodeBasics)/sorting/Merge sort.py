def merge_sort(arr):  # O(nlogn)
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_tow_sorted_lists(left, right, arr)


def merge_tow_sorted_lists(a, b, arr):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1

        else:
            arr[k] = b[j]
            j += 1

        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


nums = [10, 3, 15, 7, 8, 23, 98, 29]
merge_sort(nums)
print(nums)