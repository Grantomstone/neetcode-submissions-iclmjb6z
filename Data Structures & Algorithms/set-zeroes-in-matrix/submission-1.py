class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        M, N = len(matrix), len(matrix[0])

        rowZero = False

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        
        for i in range(1,M):
            for j in range(1,N):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(M):
                matrix[i][0] = 0
        
        if rowZero:
            for j in range(N):
                matrix[0][j] = 0
                
        