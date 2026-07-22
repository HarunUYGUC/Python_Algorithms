# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Example usage:
# Constructing a binary tree:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Run the invertTree function
solution = Solution()
inverted_root = solution.invertTree(root)

# Function to print the tree in-order for verification
def print_in_order(node):
    if node:
        print_in_order(node.left)
        print(node.val, end=" ")
        print_in_order(node.right)

# Print the inverted binary tree in-order
print_in_order(inverted_root)
