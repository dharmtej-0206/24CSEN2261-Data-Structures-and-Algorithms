class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


def level_order(root):
    if not root:
        return
    queue = [root]  

    while queue:
        node = queue.pop(0)  
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print("Preorder Traversal:")
preorder(root) 
print("\nInorder Traversal:")
inorder(root)   
print("\nPostorder Traversal:")
postorder(root) 
print("\nLevel Order Traversal:")
level_order(root) 
