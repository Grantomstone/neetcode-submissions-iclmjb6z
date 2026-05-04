# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        output = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            maxLeft = max(dfs(root.left), 0)
            maxRight = max(dfs(root.right), 0)
            
            rootMax = root.val + maxLeft + maxRight
            output[0] = max(rootMax, output[0])

            return root.val + max(maxRight, maxLeft)
        
        dfs(root)
        return output[0]
            


        
