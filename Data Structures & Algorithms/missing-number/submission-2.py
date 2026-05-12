class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            output ^= i
            output ^= nums[i]
            print(f"{i=} {nums[i]=}")
        output ^= len(nums)
        
        return output