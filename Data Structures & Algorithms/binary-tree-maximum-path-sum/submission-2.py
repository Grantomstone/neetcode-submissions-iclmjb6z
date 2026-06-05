# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxNum = float("-inf")
        
        def dfs(root):
            nonlocal maxNum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            localMax = left + right + root.val
            if localMax > maxNum:
                maxNum = localMax
            return max(left, right) + root.val
        
        dfs(root)
        return maxNum

            