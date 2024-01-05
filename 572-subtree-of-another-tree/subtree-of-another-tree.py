# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            print("p, q", p.val if p else None, q.val if q else None)
            if not p and not q:
                return True
            if (not p) or (not q):
                return False
            if p.val != q.val:
                return False
            if not isSameTree(p.left, q.left):
                return False
            return isSameTree(p.right, q.right)
        
        def dfs(node, subRoot):
            if isSameTree(node, subRoot):
                return True
            elif node and subRoot:
                return dfs(node.left, subRoot) or dfs(node.right, subRoot)
            return False

        return dfs(root, subRoot)