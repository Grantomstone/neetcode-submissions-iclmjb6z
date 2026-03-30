class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1list = [0] * 26
        for ch in s1:
            s1list[ord(ch) - ord('a')] += 1

        checklist = [0] * 26
        for i in range(len(s1)):
            checklist[ord(s2[i]) - ord('a')] += 1

        if s1list == checklist:
            return True

        for i in range(len(s1), len(s2)):
            checklist[ord(s2[i]) - ord('a')] += 1
            checklist[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if s1list == checklist:
                return True
        return False
            

