def factorial(n):  # time: T(n) = 3n + 1 --> O(n)
    if n <= 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)  # this line will be: n * (n - 1)!


def main():
    print(factorial(int(input())))


if __name__ == '__main__':
    main()


# Recursion used for : print notes of a tree, DFS on a graph, Quick sort, Merge sort, a big problem needs to be small problems
