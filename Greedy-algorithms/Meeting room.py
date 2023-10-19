def solve(meetings):
    data = []
    for s, e in meetings:
        data.append((s, 1))
        data.append((e, -1))

    data.sort()

    curr = 0
    _max = 0
    for _, v in data:
        curr += v
        _max = max(_max, curr)

    return _max


meeting = [[5, 10], [15, 20], [0, 30]]
print(solve(meeting))