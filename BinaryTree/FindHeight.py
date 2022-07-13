""" Find Height of BinaryTree """


class Node:

    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Height(rootNode):
    """ Find Height of Binary Tree """

    if rootNode is None:
        return 0

    lh = Height(rootNode.left)
    lr = Height(rootNode.right)

    return 1 + max(lr, lh)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

BinaryTree_Height = Height(root)
