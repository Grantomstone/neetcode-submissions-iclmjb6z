class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, i_value in enumerate(nums):
            for j, j_value in enumerate(nums[i:]):
                if i != j+i and i_value + j_value == target:
                    return [i, j+i]

                    


        