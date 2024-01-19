# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(a, b):
            if a and b:
                return a.val == b.val and equal(a.left, b.left) and equal(a.right, b.right)
            else:
                return a == b
        left, right = False, False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        return equal(root, subRoot) or left or right
