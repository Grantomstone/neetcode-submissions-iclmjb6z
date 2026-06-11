class Solution:
    def integerBreak(self, n: int) -> int:
        
        cache = [0] * (n+1)
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = 0 if i == n else i
            for j in range(1, i):
                cache[i] = max(cache[i], cache[j] * cache[i - j])
        
        return cache[n]
        
        cache = {1:1}
        def dfs(num):
            if num in cache:
                return cache[num]
            
            cache[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                cache[num] = max(cache[num], val)
            return cache[num]
        return dfs(n)