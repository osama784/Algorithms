# inefficient:

def min_subarray_sum(array):  # O(N square)
    if len(array) == 0:
        return 0

    min_sum = float('inf')  # infinity

    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            subarray = array[i:j]
            min_sum = min(min_sum, sum(subarray))

    return min_sum


# Dynamic:


def solve(array):
    if len(array) == 0:
        return 0

    min_sum_using_element = [array[0]]
    min_sum = array[0]

    for i in range(1, len(array)):
        num = array[i]
        current_min = min(num, num + min_sum_using_element[i - 1])
        min_sum_using_element.append(current_min)
        min_sum = min(min_sum, current_min)

    return min_sum


print(solve([-7, 3, 4, -2, -3, 1, -3]))
print(solve([20, -7, -3, 9]))

# or:


def solve(array):
    if len(array) == 0:
        return 0

    min_sum_using_last_element = array[0]
    min_sum = array[0]

    for i in range(1, len(array)):
        num = array[i]
        current_min = min(num, num + min_sum_using_last_element)
        min_sum_using_last_element = current_min
        min_sum = min(min_sum, current_min)

    return min_sum


print(solve([-7, 3, 4, -2, -3, 1, -3]))

