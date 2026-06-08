class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        sums = set([0])
        target = sum(nums) // 2

        for i in nums:
            temp = set()
            for t in sums:
                if t + i == target:
                    return True
                temp.add(t + i)
                print(t + i)
                temp.add(t)
            sums = temp
        return False