# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkEquality(root1 : Optional[TreNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return checkEquality(root1.left, root2.left) and checkEquality(root1.right, root2.right)
        
        stack = [root]

        while stack:
            node = stack.pop()
            if checkEquality(node, subRoot):
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)
        
        return False
        