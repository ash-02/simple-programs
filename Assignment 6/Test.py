class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Example usage:
if __name__ == "__main__":
    root = None
    keys = [5, 3, 7, 2, 4, 6, 8]
    for key in keys:
        root = insert(root, key)

    # Function to traverse and print the binary tree in inorder traversal order
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.key, end=" ")
            inorder_traversal(root.right)

    print("Inorder traversal of the constructed binary tree:")
    inorder_traversal(root)
