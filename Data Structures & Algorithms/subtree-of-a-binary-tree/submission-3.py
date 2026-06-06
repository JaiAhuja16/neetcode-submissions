# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def f(node):
            if not node:
                return '!'
            return f"[{node.val}{f(node.left)}{f(node.right)}]"
        s1 = f(root)
        s2 = f(subRoot)
        # print(s1)
        # print(s2)
        return s2 in s1