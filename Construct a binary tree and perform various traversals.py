# Class representing a node in a binary tree
class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.value = key  # Value of the node


# Function for Preorder Traversal (Root -> Left -> Right)
def preorder(root):
    if root:
        print(root.value, end=" ")  # Print the root node
        preorder(root.left)  # Recur on left subtree
        preorder(root.right)  # Recur on right subtree


# Function for Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)  # Recur on left subtree
        print(root.value, end=" ")  # Print the root node
        inorder(root.right)  # Recur on right subtree


# Function for Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    if root:
        postorder(root.left)  # Recur on left subtree
        postorder(root.right)  # Recur on right subtree
        print(root.value, end=" ")  # Print the root node


# Function for Level Order Traversal (Breadth-First Traversal)
def level_order(root):
    if not root:
        return
    queue = [root]  # Initialize queue with root node

    while queue:
        node = queue.pop(0)  # Dequeue node from the front
        print(node.value, end=" ")  # Print the node value

        if node.left:
            queue.append(node.left)  # Enqueue left child
        if node.right:
            queue.append(node.right)  # Enqueue right child


# Creating the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Performing different tree traversals
print("Preorder Traversal:")
preorder(root)  # Expected output: 1 2 4 5 3 6 7

print("\nInorder Traversal:")
inorder(root)   # Expected output: 4 2 5 1 6 3 7

print("\nPostorder Traversal:")
postorder(root)  # Expected output: 4 5 2 6 7 3 1

print("\nLevel Order Traversal:")
level_order(root)  # Expected output: 1 2 3 4 5 6 7
