class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minlength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlength] == w2[:minlength]:
                return ""
            for j in range(minlength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        output = []

        def dfs(ch):
            if ch in visited:
                return visited[ch]
            
            visited[ch] = True
            for b in adj[ch]:
                if dfs(b):
                    return True
            visited[ch] = False
            output.append(ch)
        
        for ch in adj:
            if dfs(ch):
                return ""
        
        output.reverse()
        return "".join(output)