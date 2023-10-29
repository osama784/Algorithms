class Treenode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + '(' + self.designation + ')'
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_management_tree():

    root = Treenode('Nilupul', 'CEO')

    chinmay = Treenode('Chinmay', 'CTO')

    vishwa = Treenode('Vishwa', 'Infrastructure Head')
    vishwa.add_child(Treenode('Dhaval', 'Cloud Manager'))
    vishwa.add_child(Treenode('Abhijit', 'App Manager'))
    amir = Treenode('Amir', 'Application Head')
    chinmay.add_child(vishwa)
    chinmay.add_child(amir)

    gels = Treenode('Gels', 'HR Head')
    gels.add_child(Treenode('Peter', 'Recruitment'))
    gels.add_child(Treenode('Waqas', 'Policy Manager'))

    root.add_child(chinmay)
    root.add_child(gels)

    return root


if __name__ == '__main__':
    root = build_management_tree()

    root.print_tree(input())