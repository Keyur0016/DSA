""" Find Left View of BinaryTree """


class Node:

    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(rootNode):
    Q1 = [rootNode]
    Q2 = []

    Tree = []
    Level = []

    while len(Q1) != 0 or len(Q2) != 0:
        while len(Q1) != 0:
            CurrentNode = Q1[0]
            Q1.pop(0)

            # Add RootNode value in LevelList
            Level.append(CurrentNode.data)

            if CurrentNode.left is not None:
                Q2.append(CurrentNode.left)

            if CurrentNode.right is not None:
                Q2.append(CurrentNode.right)

        Tree.append(Level[::])
        Level.clear()

        while len(Q2) != 0:
            CurrentNode = Q2[0]
            Q2.pop(0)

            # Add RootNode value in LevelList
            Level.append(CurrentNode.data)

            if CurrentNode.left is not None:
                Q1.append(CurrentNode.left)

            if CurrentNode.right is not None:
                Q1.append(CurrentNode.right)

        Tree.append(Level[::])
        Level.clear()

    Tree.pop(len(Tree) - 1)
    return Tree


def LeftView(Leveltree):
    """ Function is print LeftView of BinaryTree """

    LeftViewTree = []

    for item in Leveltree:
        LeftViewTree.append(item[0])

    return LeftViewTree


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

LevelTree = LevelOrderTraversal(root)
LeftViewTree = LeftView(LevelTree)

