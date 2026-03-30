class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.create_comparable(s)
        t_dict = self.create_comparable(t)
        return s_dict == t_dict


    def create_comparable(self, string: str) -> dict:
        output = {}
        for char in string:
            if char not in output:
                output[char] = 1
            else:
                output[char] += 1
        return output
        