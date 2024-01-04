# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)] # node, visited
        depths = {}
        diameter = 0
        while stack:
            node, visited = stack.pop()
            if visited:
                left_depth = depths[node.left] if node.left else 0 
                right_depth = depths[node.right] if node.right else 0 
                diameter = max(diameter, left_depth + right_depth)
                depths[node] = 1 + max(left_depth, right_depth)
            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        return diameter
