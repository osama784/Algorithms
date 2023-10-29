from collections import deque

prices = deque()

# prices.appendleft(5)
# prices.appendleft(27)
# prices.appendleft(10)
# print(prices)
# prices.pop()
# print(*prices)

while True:
    if len(prices) == (1 or 0):
        break
    elif len(prices) >= 2:
        prices.pop()

prices.appendleft({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
    })

prices.appendleft({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
    })


class Queue:
    def __init__(self): # you could write the rest functions
        self.stocks = deque()

    def is_empty(self):
        return len(self.stocks) == 0

    def size(self):
        return len(self.stocks)


stocks = Queue()
