class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        adj = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 -x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        total_cost = 0
        visited = set()
        heap = [(0,0)]
        while len(visited) < N:
            cost, ind = heapq.heappop(heap)
            if ind in visited:
                continue
            total_cost += cost
            visited.add(ind)
            for n_cost, n_ind in adj[ind]:
                if n_ind not in visited:
                    heapq.heappush(heap, (n_cost, n_ind))
        return total_cost