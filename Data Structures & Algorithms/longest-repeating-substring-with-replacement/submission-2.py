class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = {}
        output = 0
        maxF = 0
        l = 0
        for r in range(len(s)):
            charset[s[r]] = charset.get(s[r], 0) + 1
            maxF = max(maxF, charset[s[r]])
            if (r - l + 1) - maxF > k:
                charset[s[l]] = charset[s[l]] - 1
                l += 1
            output = max(output, r-l + 1)
        return output
        



