class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, ival in enumerate(nums):
            for m, jval in enumerate(nums[i+1:]):
                j = i + m + 1
                if ival + jval == target:
                    return [i,j]