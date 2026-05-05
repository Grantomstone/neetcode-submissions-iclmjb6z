import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def __setitem__(self, a, b):
        self.children[a] = b
    
    def __getitem__(self, a):
        return self.children.get(a, None)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node[ch]:
                node[ch] = TrieNode()
            node = node[ch]
        node.end = True

    def search(self, word: str) -> bool:        
        def dfs(j, root):
            node = root

            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if not node[ch]:
                        return False
                    node = node[ch]
            return node.end
        return dfs(0, self.root)