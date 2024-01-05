class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            if node:
                stack.extend([(node.right, level + 1), (node.left, level + 1)])
                result[level].append(node.val)

        return list(result.values())