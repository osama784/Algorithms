def min_val(arr):
    minvalue = arr[0]

    for i in range(1, len(arr)):  # without index 0 cause we supposed that it is the min & without last index
        if arr[i] < minvalue:
            minvalue = arr[i]

    return minvalue


nums = [23, 45, 67, 78, 24, 5, 28, 18]

print(min_val(nums))


def min_val_index(arr):
    minvalueind = 0
    minvalue = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minvalue:
            minvalue = arr[i]
            minvalueind = i

    return minvalueind


print(min_val_index(nums))

