class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        # search base node
        if self.data == val:
            return True

        # search left tree
        elif val < self.data:
            # the value might be in the left subtree
            if self.left:
                return self.left.search(val)
            else:  # if the value isn't in the tree
                return False
        # search right tree
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])  # we considered the first element will be the mother node

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 1, 18]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(18))
    countries = ['Uk', 'India', 'Pakistan', 'China', 'USA', 'Germany']
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print(countries_tree.search('Uk'))
