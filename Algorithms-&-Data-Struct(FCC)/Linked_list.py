class Node:
    """
    An object for storing node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None  # Global variable
    next_node = None  # just in the current time, just to make a variable the reference don't matter

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data


N1 = Node(10)
print(N1)
N2 = Node(20)
N1.next_node = N2  # N1 points to N2
print(N1.next_node)


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None  # just in the current time, just to make a variable the reference doesn't matter
                          # it represents the Node: N1, N2 and so on

    def is_empty(self):
        return self.head is None  # or == None

    def size(self):
        """
         Returns the number of nodes in the list
         Takes O(n) time  (Linear time)
        """
        current = self.head
        count = 0

        while current:  # the same: current !=None
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) constant time
        """
        new_node = Node(data)  # like N1
        new_node.next_node = self.head  # like N2 above
        self.head = new_node  # without this line, nothing will be added

    def search(self, key):
        """
        Search for the first node containing data the matches the key
        Return the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head  # local variable

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Insert a new node containing data at index position
        Insertion takes O(1) constant time but finding the node at the insertion point takes O(n)
        Takes overall linear time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next_no = current.next_node

            prev.next_node = new
            new.next_node = next_no

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) Time (because in the worst case scenario we need to search th entire list)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:  # while current : we didn't reach the tail, while not found: obvious
            if current.data == key and current is self.head:  # a special case because there is no node before the head points to it
                found = True
                self.head = current.next_node  # so the head get removed and the next node becomes the head
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    # def remove_index(self, data, index):
    #     current = self.head
    #
    #     if index == 0:
    #         self.remove(data)
    #         current.next_node = self.head
    #
    #     if index > 0:
    #         removed = Node(data)
    #
    #         position = index
    #         current = self.head
    #
    #         while position > 1:
    #             current.next_node = current
    #             position -= 1
    #
    #         prev = current.next_node
    #         next_no = current
    #
    #         prev.next_node = removed
    #         removed.next_node = next_no

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head  # local variable

        while current:  # means while the current isn't a tail
            if current is self.head:
                nodes.append(f'[Head:{current.data}]')
            elif current.next_node is None:
                nodes.append(f'[Tail:{current.data}]')
            else:
                nodes.append(f'[{current.data}]')

            current = current.next_node
        return '-> '.join(nodes)


l = LinkedList()
l.head = N1
print(l.size())
l.add(1)
l.add(2)
print(l.size())
print(l)
print(l.search(10))
print(l)
l.remove(2)
print(l)

