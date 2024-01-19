# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(node):
            if not node:
                return 0
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            return 1 + max(left_depth, right_depth)
        def dfs(node, max_diameter):
            if not node:
                return max_diameter
            diameter = max_depth(node.left) + max_depth(node.right)
            max_diameter =  max(max_diameter, diameter)
            return max(max_diameter, dfs(node.left, max_diameter), dfs(node.right, max_diameter))
        return dfs(root, 0)
