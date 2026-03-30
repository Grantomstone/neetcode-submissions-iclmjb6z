class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def recurse(opening, closing):
            if opening == closing == n:
                output.append("".join(stack))
                return
            
            if opening < n:
                stack.append("(")
                recurse(opening + 1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(")")
                recurse(opening, closing + 1)
                stack.pop()

        recurse(0,0)
        return output 
        
        
            
        