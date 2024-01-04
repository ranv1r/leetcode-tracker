# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.max_depth(root)
        return self.diameter

    def max_depth(self, node):
        if not node:
            return 0
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
