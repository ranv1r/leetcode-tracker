# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        while root:
            if p.val < root.val < q.val or q.val < root.val < p.val:
                return root
            elif p.val == root.val:
                return root
            elif q.val == root.val:
                return root
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                root = root.left
        return lca