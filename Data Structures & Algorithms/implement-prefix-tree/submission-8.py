class PrefixNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26
    
    def __setitem__(self, a: str, b):
        self.children[ord(a) - ord('a')] = b

    def __getitem__(self, a):
        return self.children[ord(a) - ord('a')]

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node[ch]:
                node[ch] = PrefixNode()
            node = node[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if node[ch] == None:
                return False
            node = node[ch]
        return node.end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if node[ch] == None:
                return False
            node = node[ch]
        return True
        