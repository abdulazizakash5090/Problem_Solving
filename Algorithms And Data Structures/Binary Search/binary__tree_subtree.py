class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1, root2):

    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is None:
        return False

    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right)
            )


def isSubtree(T, S):

    if S is None:
        return True

    if T is None:
        return False

    if (areIdentical(T, S)):
        return True

    return isSubtree(T.left, S or isSubtree(T.right, S))


T = Node(1)
T.right = Node(2)
T.right.right = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)


S = Node(10)
S.right = Node(6)
S.left = Node(6)
S.left.right = Node(30)

if isSubtree(T, S):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")


MAX = 100


class Node:

    def __init__(self):
        self.key = ' '
        self.left = None
        self.right = None


def newNode(item):
    temp = Node()
    temp.key = item
    return temp


def storeInorder(root, i):
    if (root == None):
        return '$'
    res = storeInorder(root.left, i)
    res += root.key
    res += storeInorder(root.right, i)
    return res


def storePreOrder(root, i):
    if (root == None):
        return '$'
    res = root.key
    res += storePreOrder(root.left, i)
    return res


def isSubtree(T, S):

    if (S == None):
        return True
    if (T == None):
        return False

    m = 0
    n = 0
    inT = storeInorder(T, m)
    inS = storeInorder(S, n)

    res = True
    if inS in inT:
        res = True
    else:
        res = False
    if (res == False):
        return res

    m = 0
    n = 0
    preT = storePreOrder(T, m)
    preS = storePreOrder(S, n)

    if preS in preT:
        return True
    else:
        return False


T = newNode('a')
T.left = newNode('b')
T.right = newNode('d')
T.left.left = newNode('c')
T.right.right = newNode('e')

S = newNode('a')
S.left = newNode('b')
S.left.left = newNode('c')
S.right = newNode('d')


if (isSubtree(T, S)):
    print("Yes: S is a subtree of T")
else:
    print("No: S is Not a subtree of T")
