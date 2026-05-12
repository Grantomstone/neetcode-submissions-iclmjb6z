class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        M, N = len(matrix), len(matrix[0])

        rowHash, colHash = set(), set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rowHash.add(i)
                    colHash.add(j)
        
        for i in range(M):
            for j in range(N):
                if i in rowHash or j in colHash:
                    matrix[i][j] = 0
        