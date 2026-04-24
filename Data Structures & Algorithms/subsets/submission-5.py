class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subsets = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                output.append(subsets.copy())
                return

            dfs(i + 1)
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()

        dfs(0)
        return output
