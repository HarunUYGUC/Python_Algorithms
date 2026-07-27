# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(root1, root2))
