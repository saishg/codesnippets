# https://www.careercup.com/question?id=5074469692375040


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def max_even_sum(self, sum_of_values=0):
        sum_of_values += self.value

        if self.left is None and self.right is None:
            if sum_of_values % 2 == 0:
                return sum_of_values
            else:
                return 0

        if self.left:
            left_sum = self.left.max_even_sum(sum_of_values)
        if self.right:
            right_sum = self.right.max_even_sum(sum_of_values)

        return max(left_sum, right_sum)
        

    def display(self):
        if self.left:
            self.left.display()
        print self.value
        if self.right:
            self.right.display()


if __name__ == '__main__':
    root = Node(7)
    root.add(Node(5))
    root.add(Node(6))
    root.add(Node(4))
    root.add(Node(9))
    root.add(Node(8))
    root.add(Node(10))
#    root.display()
    print root.max_even_sum()
