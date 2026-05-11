class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        data = [[0 for _ in range(n+1)] for _ in range(m+1)]
        data[m-1][n-1] = 1

        for i in range(m-1, -1,-1):
            for j in range(n - 1, -1, -1):
                data[i][j] += data[i+1][j] + data[i][j+1]
        
        return data[0][0]
