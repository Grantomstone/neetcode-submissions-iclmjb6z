class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]) )
        
    def helper(self, nums: List[int]) -> int:
        one = nums[0]
        two = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            curr = max(two, nums[i] + one)
            one = two
            two = curr
        return two