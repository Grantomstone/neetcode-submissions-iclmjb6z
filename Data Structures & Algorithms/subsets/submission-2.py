class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subsets = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                output.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)

        dfs(0)
        return output
