# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def f(node):
            nonlocal res
            if node:
                h1 = f(node.left) + 1
                h2 = f(node.right) + 1
                res &= abs(h1 - h2) <= 1
                return max(h1, h2)
            else:
                return 0
        f(root)
        return res