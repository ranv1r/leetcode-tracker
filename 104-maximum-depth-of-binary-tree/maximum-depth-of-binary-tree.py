# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodes = [(root, 1)]
        max_depth = 0
        while nodes:
            node, curr_depth = nodes.pop()
            if not node:
                continue
                
            child_depth = curr_depth + 1
            nodes.append((node.left, child_depth))
            nodes.append((node.right, child_depth))

            max_depth = max(max_depth, curr_depth)
        return max_depth

