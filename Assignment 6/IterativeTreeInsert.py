class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_insert(root, key):
    y = None
    x = root
    while x is not None:
        y = x
        if key < x.key:
            x = x.left
        else:
            x = x.right
    new_node = TreeNode(key)
    if y is None:
        root = new_node
    elif key < y.key:
        y.left = new_node
    else:
        y.right = new_node
    return root

# Example usage:
if __name__ == "__main__":
    # Example tree:     4
    #                  / \
    #                 2   7
    #                / \ / \
    #               1  3 6  9
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Before insertion:")
    print("Tree:", root)

    root = tree_insert(root, 5)

    print("\nAfter insertion:")
    print("Tree:", root)
