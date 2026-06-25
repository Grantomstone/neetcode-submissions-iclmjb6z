class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0

        for i in nums:
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 += 1
            else:
                count2 += 1
    
        i = 0
        while i < count0:
            nums[i] = 0
            i += 1
        while i < count0 + count1:
            nums[i] = 1
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1
        
    