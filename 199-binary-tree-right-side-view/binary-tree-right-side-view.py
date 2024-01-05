# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversl
        queue = deque([(root, 0)]) # node, level
        levels = defaultdict(list)
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            levels[level].append(node.val)
            # Append left first since queue if FIFO
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        # return list that contains right most node in each level
        return [level[-1] for level in levels.values()]
