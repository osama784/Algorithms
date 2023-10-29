def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)  # we gave the function a new list to work with
            else:
                return recursive_binary_search(list[:midpoint], target)  # :midpoint means start at beginning to midpoint


def verify(result):
    print('Target found:', result)


numbers = [i + 1 for i in range(8)]
result = recursive_binary_search(numbers, 5)
verify(result)