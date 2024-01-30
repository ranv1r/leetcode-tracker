# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path(node):
            if not node:
                return 0, float('-inf')
            left, left_max = max_path(node.left)
            right, right_max = max_path(node.right)
            left = max(left, 0)
            right = max(right, 0)
            return (
                node.val + max(left, right),
                max(node.val + left + right, left_max, right_max)
            )
        mp = max_path(root)[1]
        return mp if mp != float('-inf') else 0
        