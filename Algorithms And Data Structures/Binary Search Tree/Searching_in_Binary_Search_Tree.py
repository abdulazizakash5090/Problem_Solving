class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node


def search(root, key):

    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)

    return search(root.left, key)


if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    key = 6

    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")

    key = 60

    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
