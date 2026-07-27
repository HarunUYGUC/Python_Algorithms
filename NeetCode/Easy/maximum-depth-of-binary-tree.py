# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)
root.right.left = TreeNode(4)

solution = Solution()
print(solution.maxDepth(root))
