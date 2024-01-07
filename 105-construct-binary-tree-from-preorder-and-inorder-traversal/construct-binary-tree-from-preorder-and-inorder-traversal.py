# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        n = TreeNode(preorder[0])
        l = inorder.index(preorder[0]) if preorder[0] in inorder else -1
        if l != -1:
            n.left = self.buildTree(preorder[1:l + 1], inorder[:l])
            n.right = self.buildTree(preorder[l + 1:], inorder[l + 1:])
        else:
            n.right = self.buildTree(preorder[1:], inorder[1:])
        return n