class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  # without this line : there will not be a parent
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:  # means : len(self.children) != 0
            for child in self.children:
                child.print_tree()



def build_product_tree():
    root = Treenode('Electronics')

    laptop = Treenode('Laptop')
    laptop.add_child(Treenode('Mac'))
    laptop.add_child(Treenode('Surface'))
    laptop.add_child(Treenode('Thinkpad'))

    cellphone = Treenode('Cell Phone')
    cellphone.add_child(Treenode('iPhone'))
    cellphone.add_child(Treenode('Google Pixel'))
    cellphone.add_child(Treenode('Vivo'))

    tv = Treenode('TV')
    tv.add_child(Treenode('Samsung'))
    tv.add_child(Treenode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()