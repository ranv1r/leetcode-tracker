# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([(root, False)]) # tuple(node, left_visited)
        i, last = 0, 0
        while i != k:
            n, lv = q.popleft()
            if n:
                if lv:
                    i += 1
                    last = n.val
                else:
                    q.appendleft((n.right, False))
                    q.appendleft((n, True))
                    q.appendleft((n.left, False))
        return last