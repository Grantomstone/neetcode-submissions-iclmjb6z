class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        if not edges:
            return True
        
        adjecency = {i: [] for i in range(n)}

        for a,b in edges:
            adjecency[a].append(b)
            adjecency[b].append(a)
        
        cycle = set()
        max_length = 0
        def hasCycle(node: int, prev: int) -> bool:
            if node in cycle:
                return True
            
            cycle.add(node)
            for neigh in adjecency[node]:
                if neigh == prev:
                    continue 
                if hasCycle(neigh, node):
                    return True
            return False
        
        return not hasCycle(0, -1) and n == len(cycle)