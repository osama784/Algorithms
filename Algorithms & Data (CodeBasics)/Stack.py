from collections import deque


class Stack:  # LIFO : Last in First out
    def __init__(self):
        self.container = deque()  # or a list instead

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def __repr__(self):
        return f'{self.container}'


s = Stack()
s.push(5)
s.push(48)
s.push('op')
print(s.size())
s.pop()
print(s)
print(s.is_empty())