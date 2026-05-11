import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        heap = [(grid[0][0], 0, 0)]
        visited.add((0,0))
        while heap:
            height, row, col = heapq.heappop(heap)
            if row == ROWS - 1 and col == COLS - 1:
                return height
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited):
                    continue
                heapq.heappush(heap, (max(grid[nr][nc], height), nr, nc))
                visited.add((nr,nc))
        return -1
        