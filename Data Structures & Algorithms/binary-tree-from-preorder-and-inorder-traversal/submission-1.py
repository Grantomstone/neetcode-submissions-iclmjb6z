# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])
        
        inorder_map = {v: i for i, v in enumerate(inorder)}
        root_val = preorder[0]
        preorder = preorder[1:]
        inorder_index = inorder_map[root_val]
        left = inorder[:inorder_index]
        right = inorder[inorder_index + 1:]

        root = TreeNode(root_val)
        if left:
            root.left = self.buildTree(preorder[:len(left)],left)
        if right:
            root.right = self.buildTree(preorder[len(left):], right)
        return root