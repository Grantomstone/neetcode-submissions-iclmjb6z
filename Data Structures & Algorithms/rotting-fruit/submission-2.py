from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        total_banans = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    total_banans += 1
                elif grid[r][c] == 1:
                    total_banans += 1
        
        if len(q) == 0:
            if total_banans > 0:
                return -1
            return 0
        
        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or(nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))
            time += 1
        
        if len(visited) != total_banans:
            return -1
        return time
                    
                    