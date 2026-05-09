class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        output = 0
        while r < len(nums) -1:
            farthest = 0
            for i in range(l,r+1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]
            l = r+1
            r = farthest
            output +=1
        return output
                