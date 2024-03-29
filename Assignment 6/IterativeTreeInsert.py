# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.parent = None

# def recursive_tree_insert(root, new_node):
#     if root is None:
#         root = new_node
#     else:
#         if new_node.key < root.key:
#             next_node = root.left
#         else:
#             next_node = root.right
#         if next_node is None:
#             if new_node.key < root.key:
#                 root.left = new_node
#             else:
#                 root.right = new_node
#             new_node.parent = root
#         else:
#             recursive_tree_insert(next_node, new_node)
#     return root

# def binary_tree_insert(root, new_node):
#     y = None
#     x = root
#     while x is not None:
#         y = x
#         if new_node.key < x.key:
#             x = x.left
#         else:
#             x = x.right

#     new_node.parent = y
#     if y is None:
#         root = new_node
#     elif new_node.key < y.key:
#         y.left = new_node
#     else:
#         y.right = new_node

#     return root

# def display_tree(root):
#     if root is not None:
#         display_tree(root.left)
#         print(root.key)
#         display_tree(root.right)

# root = None
# root = CheckIfRoot(root, TreeNode(5))
# main_root = root
# root = CheckIfRoot(root, TreeNode(3))
# root = CheckIfRoot(root, TreeNode(7))
# root = CheckIfRoot(root, TreeNode(2))
# root = CheckIfRoot(root, TreeNode(4))
# root = CheckIfRoot(root, TreeNode(6))
# root = CheckIfRoot(root, TreeNode(8))
# display_tree(main_root)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None  # Parent pointer added for testing purposes

def Recursive_Tree_Insert(T, current_parent, new_node):
    if T.root is None:
        T.root = new_node
        new_node.parent = None
    else:
        if new_node.key < current_parent.key:
            next_node = current_parent.left
        else:
            next_node = current_parent.right
        if next_node is None:
            if new_node.key < current_parent.key:
                current_parent.left = new_node
            else:
                current_parent.right = new_node
            new_node.parent = current_parent
        else:
            Recursive_Tree_Insert(T, next_node, new_node)

def print_inorder(node):
    if node is not None:
        print_inorder(node.left)
        print(node.key, end=' ')
        print_inorder(node.right)

# Create an empty binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

# Test the Recursive_Tree_Insert function
bst = BinarySearchTree()
Recursive_Tree_Insert(bst, bst.root, TreeNode(5))
Recursive_Tree_Insert(bst, bst.root, TreeNode(3))
Recursive_Tree_Insert(bst, bst.root, TreeNode(7))
Recursive_Tree_Insert(bst, bst.root, TreeNode(4))
Recursive_Tree_Insert(bst, bst.root, TreeNode(6))
Recursive_Tree_Insert(bst, bst.root, TreeNode(8))

# Print the binary search tree in inorder traversal
print("Inorder traversal of the binary search tree:")
print_inorder(bst.root)
