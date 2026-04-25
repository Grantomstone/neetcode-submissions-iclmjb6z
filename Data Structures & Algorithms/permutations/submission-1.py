class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(data: List[int], nums: set) -> None:
            if len(nums) == 0:
                output.append(data)
                return
            
            for i in nums:
                b = nums.copy()
                b.remove(i)
                dfs([*data, i],b)
        
        dfs([], set(nums))
        return output

            