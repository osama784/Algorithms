from collections import deque


def reverse(string):
    d_string = deque()
    for i in string:
        d_string.appendleft(i)
    print(*d_string, sep='')


reverse(input())


# s2:

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquer COVID-19"))
    print(reverse_string("I am the king"))
