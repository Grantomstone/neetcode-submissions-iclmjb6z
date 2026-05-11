class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def traverse(i, total):
            if i == len(nums):
                return total == target
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            output = traverse(i+1, (total + nums[i])) + traverse(i+1, total - nums[i])
            cache[(i, total)] = output
            return output
        
        return traverse(0, 0)