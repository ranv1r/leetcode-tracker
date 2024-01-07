# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        gc = 0
        q = deque([(root, root.val)]) # n, m
        while q:
            n, m = q.popleft()
            if n:
                if m <= n.val:
                    gc += 1
                if n.left:
                    q.append((n.left, max(m, n.left.val)))
                if n.right:
                    q.append((n.right, max(m, n.right.val)))
        return gc
                

