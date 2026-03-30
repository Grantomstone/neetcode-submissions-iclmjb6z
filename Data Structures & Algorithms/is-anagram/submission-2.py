class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.create_comparable(s)
        t_dict = self.create_comparable(t)
        return s_dict == t_dict


    def create_comparable(self, string: str) -> dict:
        output = {}
        for char in string:
            output[char] = 1 + output.get(char, 0)
        return output
        