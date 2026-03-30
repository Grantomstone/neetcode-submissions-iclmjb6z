class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        hash = {}

        for string in strs:
            dict_key = [0] * 26
            for char in string:
                dict_key [ord(char) - ord("a")] += 1
            if tuple(dict_key) not in hash:
                hash[tuple(dict_key)] = [string]
            else:
                hash[tuple(dict_key)].append(string)
        return hash.values()
            