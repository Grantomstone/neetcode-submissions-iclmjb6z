class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        sort_nums = sorted(nums)
        for index, num in enumerate(sort_nums):
            if index > 0 and num == sort_nums[index - 1]:
                continue
            l, r = index + 1, len(sort_nums) - 1
            while l < r:
                sum3 = num + sort_nums[l] + sort_nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    output.append([num, sort_nums[l], sort_nums[r]])
                    l += 1
                    while sort_nums[l] == sort_nums[l - 1] and l < r:
                        l += 1
        
        return output