class Solution:
    def longestPalindrome(self, s: str) -> str:
        output, length = "", 0
        for i in range(len(s)):
            # check odd palindromes
            l = r = i
            curr = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > length:
                    length = r - l + 1
                    output = s[l:r+1]
                l -= 1
                r += 1

            # cehck even palindromes
            l, r = i, i+1
            curr = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > length:
                    length = r - l + 1
                    output = s[l:r+1]
                l -= 1
                r += 1
        return output