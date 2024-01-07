class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        inorder_index = inorder.index(root_val)
        if 0 <= inorder_index < len(inorder):
            root.left = self.buildTree(preorder[1:1 + inorder_index], inorder[:inorder_index])
            root.right = self.buildTree(preorder[1 + inorder_index:], inorder[inorder_index + 1:])

        return root
