def test_inorder_tree_walk():
    # Test Tree 1
    #        5
    #       / \
    #      3   8
    #     / \ / \
    #    2  4 6  9
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    print("Test Tree 1 - Expected: 2 3 4 5 6 8 9")
    print("Actual:")
    iterative_inorder_tree_walk(root1)

    # Test Tree 2
    #       10
    #      /  \
    #     5    15
    #    / \  / \
    #   3  7 12 18
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(18)

    print("\nTest Tree 2 - Expected: 3 5 7 10 12 15 18")
    print("Actual:")
    iterative_inorder_tree_walk(root2)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def iterative_inorder_tree_walk(root):
    x = root
    stack = []
    while True:
        if x is not None:
            stack.append(x)
            x = x.left
        elif len(stack) > 0:
            x = stack.pop()
            print(x.key)
            x = x.right
        else:
            break

# Example Usage:
# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(1)

test_inorder_tree_walk()