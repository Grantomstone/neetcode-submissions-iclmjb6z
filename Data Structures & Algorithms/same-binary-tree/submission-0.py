# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p]
        parray = []
        
        while stack:
            node = stack.pop()
            if node:
                parray.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                parray.append(None)
        
        stack = [q]
        qarray = []

        while stack:
            node = stack.pop()
            if node:
                qarray.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                qarray.append(None)
        
        return parray == qarray
