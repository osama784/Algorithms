def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n)
    """

    if len(list) <= 1:  # Stopping condition
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)  # recursively
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublist - left and right

    Takes overall O(log n) time
    """
    mid = len(list)//2
    left = list[:mid]  # except the midpoint
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists , storing them in the process
    Returns a new merged list

    Runs overall O(n) time
    """
    l = []
    i = 0  # the merge count == the len(list)
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


nums = [54, 63, 17, 85, 129, 20, 6]
l = merge_sort(nums)
print(l)
print(verify_sorted(nums))
print(verify_sorted(l))










