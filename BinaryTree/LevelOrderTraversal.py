""" Horizontal level order Traversal """


class Node:

    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(rootNode):
    """ Level vise BinaryTree Traversal  """

    if rootNode is None:
        return []

    else:

        QueueTraversal = []
        Queue = [rootNode]

        while len(Queue) > 0:

            QueueTraversal.append(Queue[0].data)

            if Queue[0].left is not None:
                Queue.append(Queue[0].left)

            if Queue[0].right is not None:
                Queue.append(Queue[0].right)

            Queue.pop(0)

        return QueueTraversal


def LevelByLevelTraversal(rootNode):
    """ Print LevelByLevel Traversal of BinaryTree """

    if rootNode is None:
        return
    else:

        Q1 = [rootNode]
        Q2 = []

        Tree = []
        Level = []

        while len(Q1) != 0 or len(Q2) != 0 :
            while len(Q1) > 0:
                RootNode = Q1[0]
                Q1.pop(0)
                Level.append(RootNode.data)
                if RootNode.left is not None:
                    Q2.append(RootNode.left)
                if RootNode.right is not None:
                    Q2.append(RootNode.right)

            Tree.append(Level[::])
            Level.clear()

            while len(Q2) > 0:
                RootNode = Q2[0]
                Q2.pop(0)
                Level.append(RootNode.data)
                if RootNode.left is not None:
                    Q1.append(RootNode.left)
                if RootNode.right is not None:
                    Q1.append(RootNode.right)

            Tree.append(Level[::])
            Level.clear()

        Tree.pop(len(Tree)-1)
        return  Tree


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

LevelPrint = LevelOrderTraversal(root)
print(LevelPrint)

Tree = LevelByLevelTraversal(root)
print(Tree)