from collections import Counter

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def dfs(i: int, data: List[int], total: int) -> None:
            if total == target:
                output.append(data.copy())
                return
            
            for num in range(i, len(nums)):
                if total + nums[num] > target:
                    return
                data.append(nums[num])
                dfs(num, data, total + nums[num])
                data.pop()
        dfs(0, [], 0)

        return output