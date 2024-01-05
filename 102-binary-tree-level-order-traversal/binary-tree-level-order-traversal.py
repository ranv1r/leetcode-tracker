# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        s = [(root, 0)]
        while s:
            n, i = s.pop()
            if not n:
                continue
            s.extend([(n.right, i + 1), (n.left, i + 1)])
            if len(l) < i + 1:
                l.append([n.val])
            else:
                l[i].append(n.val)
        return l
