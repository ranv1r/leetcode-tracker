# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0, 0
            left_diameter, left_longest_arm = depth(node.left)
            right_diameter, right_longest_arm = depth(node.right)
            longest_arm = 1 + max(left_longest_arm, right_longest_arm)
            diameter = max(1 + left_longest_arm + right_longest_arm, left_diameter, right_diameter)
            return diameter, longest_arm
        return depth(root)[0] - 1
