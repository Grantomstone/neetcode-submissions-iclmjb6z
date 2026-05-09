class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        
        def traverse(r: int,c: int) -> int:
            q = deque()
            q.append((r,c))
            area = 1
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc  in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    area += 1
                    grid[nr][nc] = 0
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = traverse(r,c)
                    max_area = max(max_area, area)
        
        return max_area


