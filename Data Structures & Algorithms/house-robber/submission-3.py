class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        one = nums[0]
        two = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            curr = max(two, nums[i] + one)
            one = two
            two = curr
        return two

        