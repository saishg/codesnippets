# https://www.careercup.com/question?id=5712224583680000

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = Node(value)

    def get_levels(self, LEVELS=[], level=0):
        if level >= len(LEVELS):
            LEVELS.append([])

        LEVELS[level].append(self.value)

        if self.left is not None:
            self.left.get_levels(LEVELS, level+1)
        if self.right is not None:
            self.right.get_levels(LEVELS, level+1)

        return LEVELS

    def get_reversed_levels(self):
        levels = self.get_levels()
        levels.reverse()
        return levels

    def print_node(self):
        if self.left is not None:
            self.left.print_node()
        print self.value
        if self.right is not None:
            self.right.print_node()


if __name__ == '__main__':
    root = Node(50)
    root.add(25)
    root.add(12)
    root.add(20)
    root.add(37)
    root.add(40)
    root.add(75)
    root.add(90)
    root.add(100)
    root.print_node()
    print root.get_reversed_levels()

