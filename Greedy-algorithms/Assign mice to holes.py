def solve_mine(mice, holes):
    mice.sort()
    holes.sort()
    arr = []
    all_crosses = []
    for i in range(len(mice)):
        arr.append(holes[i])
        arr.append(mice[i])

    for i in range(len(arr)):
        if i % 2 == 1:
            cross = abs(abs(arr[i]) - abs(arr[i - 1]))
            all_crosses.append(cross)

    return max(all_crosses)


print(solve_mine([3, 2, -4], [0, -2, 4]))


def mice(mouse, gaps):
    mouse.sort()
    gaps.sort()

    answer = 0

    for a, b in zip(mouse, gaps):
        answer = max(answer, abs(a - b))

    return answer


print(mice([3, 2, -4], [0, -2, 4]))
