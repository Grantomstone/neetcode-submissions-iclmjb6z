class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return True
            
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            return False
        
        adj = {i: [] for i in range(1, len(edges) + 1)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited.clear()
            if dfs(a, -1):
                return [a,b]
        return []