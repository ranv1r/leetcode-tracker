# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n):
            if not n:
                return float('inf'), float('-inf'), True

            left_min, left_max, left_valid = dfs(n.left)
            right_min, right_max, right_valid = dfs(n.right)

            if not left_valid or not right_valid:
                return None, None, False

            return (
                min(left_min, right_min, n.val),
                max(left_max, right_max, n.val),
                left_max < n.val < right_min
            )

        return dfs(root)[2]
        