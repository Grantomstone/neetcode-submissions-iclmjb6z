from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digimap = {"2": list("abc"), 
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz")}

        output = [""]
        for digit in digits:
            tmp = []
            for curr in output:
                for c in digimap[digit]:
                    tmp.append(curr + c)
            output = tmp
        return output
            
            

