class Solution:
    def isPalin(self, word: str) -> bool:
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        output = []
        curr= []

        def traverse(i: int) -> None:
            if i == len(s):
                output.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s[i:j+1]):
                    curr.append(s[i:j+1])
                    traverse(j+1)
                    curr.pop()
        
        traverse(0)
        return output
