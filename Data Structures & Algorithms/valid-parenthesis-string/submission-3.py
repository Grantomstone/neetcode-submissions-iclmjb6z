class Solution:
    def checkValidString(self, s: str) -> bool:
        l=r=0
        for ch in s:
            if ch == "(":
                l,r = l+1,r+1
            elif ch == ")":
                l,r = l-1,r-1
            else:
                l,r = l-1,r+1
            if r < 0:
                return False
            if l < 0:
                l = 0
        return min(l, r) == 0