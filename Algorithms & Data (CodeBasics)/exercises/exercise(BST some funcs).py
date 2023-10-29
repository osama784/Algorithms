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

    def search(self, val):
        if self.data == val:
            return True

        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):  # myself
        if self.right:
            return self.right.find_max()

        else:
            return self.data

    def find_min(self):  # myself
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum

    def post_order(self):
        elements = []

        if self.left:
            elements += self.left.post_order()

        if self.right:
            elements += self.right.post_order()

        elements.append(self.data)

        return elements

    def pre_order(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return elements

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    nums = [17, 23, 16, 4, 78, 5, 59]
    nums_tree = build_tree(nums)

    print("Input numbers:", nums)
    print("Min:", nums_tree.find_min())
    print("Max:", nums_tree.find_max())
    print("Sum:", nums_tree.calculate_sum())
    print("In order traversal:", nums_tree.in_order_traversal())
    print("Pre order traversal:", nums_tree.pre_order())
    print("Post order traversal:", nums_tree.post_order())
    print(nums_tree.search(7))

# or:
# def find_min():
# if self.left is None:
#    return self.data
# return self.left.find_min()
