class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i, ival in enumerate(nums):
            diff_map[ival] = i
        
        for j, jval in enumerate(nums):
            diff = target - jval
            if diff in diff_map and j != diff_map[diff]:
                return [j, diff_map[diff]]