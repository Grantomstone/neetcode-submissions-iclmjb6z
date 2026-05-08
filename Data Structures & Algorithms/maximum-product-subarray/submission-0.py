class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1,1
        output = max(nums)
        for i in nums:
            if i == 0:
                currMax = currMin = 1
                continue
            tmp = currMax*i 
            currMax = max(i*currMax, i*currMin, i)
            currMin = min(tmp, i*currMin, i)
            output = max(output, currMax)
        return output