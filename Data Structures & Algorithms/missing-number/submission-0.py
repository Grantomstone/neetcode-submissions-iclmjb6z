class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)+1):
            output ^= i
        
        for i in nums:
            output ^= i
        
        return output