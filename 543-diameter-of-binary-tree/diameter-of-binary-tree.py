# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            # Base case: If the node is None, return 0 for both diameter and longest arm.
            if not node:
                return 0, 0
            
            # Recursively compute the diameter and longest arm for the left subtree.
            left_diameter, left_longest_arm = depth(node.left)
            
            # Recursively compute the diameter and longest arm for the right subtree.
            right_diameter, right_longest_arm = depth(node.right)
            
            # Calculate the length of the longest arm for the current node.
            longest_arm = 1 + max(left_longest_arm, right_longest_arm)
            
            # Calculate the diameter for the current node.
            diameter = max(1 + left_longest_arm + right_longest_arm, left_diameter, right_diameter)
            
            # Return the calculated diameter and longest arm for the current node.
            return diameter, longest_arm
        
        # The result of the depth function is a tuple, and we are interested in the diameter (index 0).
        # Subtracting 1 to get the actual number of edges in the diameter.
        return depth(root)[0] - 1

