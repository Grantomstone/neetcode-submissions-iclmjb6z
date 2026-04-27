from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digimap = {1: [], 
        2: list("abc"), 
        3: list("def"),
        4: list("ghi"),
        5: list("jkl"),
        6: list("mno"),
        7: list("pqrs"),
        8: list("tuv"),
        9: list("wxyz")}

        nums = [int(x) for x in digits]
        search = []
        for i in nums:
            search.append(digimap[i])
        out = product(*search)
        output = []
        for i in out:
            output.append("".join(i))
        return output

