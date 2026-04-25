class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        def dfs(i: int, data: List[int], total: int) -> None:
            if total == target:
                output.append(data.copy())
                return
            if total > target or i == len(candidates):
                return
            
            data.append(candidates[i])
            dfs(i + 1, data, total + candidates[i])
            data.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, data,total)
        
        dfs(0, [], 0)
        return output

