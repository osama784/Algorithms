class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self. head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # self.head = None  # if this line: the linked list will be cleared and the data list will appear
        for data in data_list:
            self.insert_at_end(data)


    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count




l = LinkedList()
l.insert_at_beginning(5)
l.insert_at_beginning(89)
l.insert_at_end(45)
l.insert_values(['banana', 'apple', 'Mango'])
l.remove_at_index(2)
l.insert_at_index(0, 'osama')
l.insert_at_index(2, 12)
l.print()
print('length:', l.get_length())