class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(eval(f"{num2} {token} {num1}"))
                stack.append(result)
        
        return stack[0]
