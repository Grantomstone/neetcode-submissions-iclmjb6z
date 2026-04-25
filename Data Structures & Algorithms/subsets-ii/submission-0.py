class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        subset = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                if subset not in output:
                    output.append(subset.copy())
                return
            
            dfs(i + 1)
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            
        
        dfs(0)
        return output