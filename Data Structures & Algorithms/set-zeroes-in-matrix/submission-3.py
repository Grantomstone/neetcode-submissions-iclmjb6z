class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        row0_is_zero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row0_is_zero = True
                    else:
                        matrix[r][0] = 0
        
        print(matrix)
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        if row0_is_zero:
            for i in range(COLS):
                matrix[0][i] = 0
