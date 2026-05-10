class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d, t in times:
            adj[s].append((d, t))
        
        heap = [(0,k)]
        visited = set()
        t = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = time
            for nu_node, nu_time in adj[node]:
                if nu_node not in visited:
                    heapq.heappush(heap, (time + nu_time, nu_node))
        
        if len(visited) == n:
            return t
        return -1
