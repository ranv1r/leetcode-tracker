# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calculate_max_path(node):
            # Base case: if the node is None
            if not node:
                return 0, float('-inf')
            
            # Recursive calls to left and right subtrees
            left_sum, left_max = calculate_max_path(node.left)
            right_sum, right_max = calculate_max_path(node.right)
            
            # Handling negative values
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            
            # Calculating the maximum path sum considering the current node
            current_sum = node.val + max(left_sum, right_sum)
            current_max = max(node.val + left_sum + right_sum, left_max, right_max)
            
            return current_sum, current_max
        
        # Calling the helper function and returning the result
        return calculate_max_path(root)[1]
        