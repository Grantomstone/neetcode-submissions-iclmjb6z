class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for x in nums:
            if x in numSet:
                return True
            else:
                numSet.add(x)
        return False

        