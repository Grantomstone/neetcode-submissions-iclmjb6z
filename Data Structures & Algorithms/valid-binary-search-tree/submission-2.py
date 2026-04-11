from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -1001, 1001)
        
    def isValid(self, node: Optional[TreeNode], minV: int, maxV: int) -> bool:
        if not node:
            return True
        else:
            if not minV < node.val < maxV:
                return False
            return self.isValid(node.left, minV, node.val) and self.isValid(node.right, node.val, maxV)