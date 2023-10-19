class node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def totalNodes(root):

    if (root == None):
        return 0

    l = totalNodes(root.left)
    r = totalNodes(root.right)

    return 1 + l + r


def newNode(data):
    Node = node(data)
    return Node


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(9)
root.left.right = newNode(8)
root.left.left.left = newNode(6)
root.left.left.right = newNode(7)

print(totalNodes(root))


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def totalNodes(root):

    if (root == None):
        return 0

    l = totalNodes(root.left)
    r = totalNodes(root.right)

    return 1 + l + r


def newNode(data):
    Node = node(data)
    return Node


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)


print(totalNodes(root))
