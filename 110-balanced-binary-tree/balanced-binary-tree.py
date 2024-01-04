# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)] # node, visited
        depths = {}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.extend([(node, True), (node.left, False), (node.right, False)])
            if node:
                ld, rd = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(ld - rd) > 1:
                    return False
                depths[node] = 1 + max(ld, rd)
        return True


