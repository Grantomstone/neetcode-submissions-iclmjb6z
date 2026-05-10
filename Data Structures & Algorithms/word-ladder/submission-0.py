class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        adj = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i+1:]
                if wildcard in adj:
                    adj[wildcard].append(word)
                else:
                    adj[wildcard] = [word]
        
        visited = set([beginWord])
        q = deque([beginWord])
        output = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return output
                for j in range(len(word)):
                    wildcard = word[:j] + "*" + word[j+1:]
                    for neigh in adj[wildcard]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            output += 1
        return 0


