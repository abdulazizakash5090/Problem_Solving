class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(root)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return TreeNode(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

# Function to perform an inorder traversal of the binary tree


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


# Creating a binary tree and adding nodes
root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 6)
root = insert(root, 8)

# Performing an inorder traversal to display the binary tree
print("Inorder Traversal:")
inorder_traversal(root)
