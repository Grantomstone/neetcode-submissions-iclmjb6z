class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hash:
                return [hash[diff], index]
            hash[value] = index
                    


        