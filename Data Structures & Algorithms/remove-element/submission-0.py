class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        length = len(nums)
        while nums.count(val) != 0:
            nums.remove(val)
            res += 1
        return length - res
        
        
        