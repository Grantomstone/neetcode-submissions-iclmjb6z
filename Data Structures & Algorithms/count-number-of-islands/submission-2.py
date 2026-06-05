class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = ((1,0), (0,1), (-1,0), (0,-1))
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def bfs(r, c):
            visited.add((r, c))
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or (nr, nc) in visited or grid[nr][nc] == '0':
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    print(visited)
        
        return islands