# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_arm(node, max_diameter):
            if not node:
                return 0
            left_arm, right_arm = 0, 0
            if node.left:
                res = max_arm(node.left, max_diameter)
                left_arm = 1 + res[0]
                max_diameter = max(max_diameter, res[1])
            if node.right:
                res = max_arm(node.right, max_diameter)
                right_arm = 1 + res[0]
                max_diameter = max(max_diameter, res[1])
            return max(left_arm, right_arm), max(max_diameter, left_arm + right_arm)
        return max_arm(root, 0)[1]