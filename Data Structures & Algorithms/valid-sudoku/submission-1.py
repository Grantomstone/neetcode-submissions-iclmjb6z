class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subBoxes = collections.defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in rows[x] or 
                    board[x][y] in cols[y] or 
                    board[x][y] in subBoxes[(x // 3, y // 3)]):
                    return False
                
                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                subBoxes[(x // 3, y // 3)].add(board[x][y])
        return True


    


        