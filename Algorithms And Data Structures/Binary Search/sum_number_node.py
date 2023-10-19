# Python3 Program to print sum of all
# the elements of a binary tree

# Binary Tree Node

""" utility that allocates a new Node
with the given key """


class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find sum of all the element


def addBT(root):
    if (root == None):
        return 0
    return (root.key + addBT(root.left) +
            addBT(root.right))


# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sum = addBT(root)

    print("Sum of all the nodes is:", sum)

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)


class NewNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def addBT(root):
    if (root == None):
        return 0
    return (root.key + addBT(root.left) + addBT(root.right))


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sum = addBT(root)

    print("Sum of all the nodes is:", sum)


def sumBT(root):

    sum = 0

    q = []

    q.append(root)

    while len(q) > 0:
        temp = q.pop(0)

        sum += temp.key

        if (temp.left != None):
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)

    return sum


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    print("Sum of all elements in the binary tree is: ", sumBT(root))
