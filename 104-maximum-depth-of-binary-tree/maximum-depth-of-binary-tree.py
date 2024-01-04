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
            nodes.extend([(node.left, curr_depth + 1), (node.right, curr_depth + 1)])
            max_depth = max(max_depth, curr_depth)
        return max_depth

