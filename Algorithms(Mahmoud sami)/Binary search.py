def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


nums = [17, 23, 45, 86, 13, 42, 77]
print(binary_search(nums, 23))