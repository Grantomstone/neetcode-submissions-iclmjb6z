class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for start, end in tickets:
            adj[start].append(end)
        
        output = ["JFK"]
        def dfs(src):
            if len(output) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                output.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i,v)
                output.pop()
            return False
        
        dfs("JFK")
        return output

         