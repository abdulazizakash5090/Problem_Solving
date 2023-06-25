# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# # A function to do inorder tree traversal
# def printPreorder(root):

#     if root:

#         # First print the data of node
#         print(root.val),

#         # Then recur on left child
#         printPreorder(root.left)

#         # Finally recur on right child
#         printPreorder(root.right)


# # Driver code
# if __name__ == "__main__":
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     # Function call
#     # print "\nInorder traversal of binary tree is"
#     printPreorder(root)

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)


def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)

        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal")
inorder(root)

print("\nPreorder traversal")
preorder(root)

print("\nPostorder traversal")
