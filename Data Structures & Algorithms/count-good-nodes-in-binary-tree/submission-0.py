# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0
        def f(node, maxi):
            nonlocal c
            if node:
                if node.val >= maxi:
                    c += 1
                    maxi = node.val
                f(node.left, maxi)
                f(node.right, maxi)
        f(root, root.val)
        return c