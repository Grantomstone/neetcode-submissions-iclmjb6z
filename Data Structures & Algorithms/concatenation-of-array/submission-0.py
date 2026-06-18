class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        for i in copy:
            nums.append(i)
        return nums