class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        output = 0
        l = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[i])
            output = max(output, i - l + 1)
        return output