class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_count = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            if nums[i] > max_count:
                max_count = nums[i]
        return max_count