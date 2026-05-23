# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global res
        res = 0
        def maxD(root):
            global res
            if root:
                l, r =  maxD(root.left), maxD(root.right)
                res = max(res, l + r)
                return 1 + max(l, r)
            else:
                return 0
        maxD(root)
        return res