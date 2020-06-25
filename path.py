import sys

MAX_PATH_SUM = -999


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self):
        pass

    def traverse(self, node):

        if node is None:
            return None

        traverse(node.left)
        print("node :", node.data)

    def path_sum(self, root):
        global MAX_PATH_SUM
        if root is None:
            return -999

        left = self.path_sum(root.left)
        right = self.path_sum(root.right)

        print("left :", left)
        print("right :", right)

        #c1 = max(max(left, right) + root.data, left, right)
        c1 = max(left, right)
        c2 = root.data
        c3 = left + root.data + right

        print("c1 :", c1)
        print("c2 :", c2)
        print("c3 :", c3)

        max_sum  = max(c1, c2, c3) # left, right)

        # max_sum  = max(c1, c2, c3, left, right)

        print("max_sum :", max_sum)

        if max_sum > MAX_PATH_SUM:
            MAX_PATH_SUM = max_sum
        return max_sum


if __name__ == '__main__':
    tree = Tree()
    tree.root =  Node(-10)
    tree.root.left = Node(9)
    tree.root.right = Node(20)

    right = tree.root.right
    right.left = Node(15)
    right.right = Node(7)

    tree2 = Tree()
    tree2.root =  Node(-10)
    tree2.root.left = Node(-9)
    tree2.root.right = Node(-20)

    right2 = tree2.root.right
    right2.left = Node(-15)
    right2.right = Node(-7)

    sum = tree.path_sum(tree.root)
    print("sum :", sum)

    print("sum :", MAX_PATH_SUM)

    # sum = tree2.path_sum(tree2.root)
    # print("sum2 :", sum)
