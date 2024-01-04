# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def dfs(node):
            if not node: return 0
            ld = dfs(node.left) # left-depth
            rd = dfs(node.right) # right-depth
            self.bal = self.bal and abs(rd - ld) <= 1
            return 1 + max(ld, rd)
        
        dfs(root)
        return self.bal