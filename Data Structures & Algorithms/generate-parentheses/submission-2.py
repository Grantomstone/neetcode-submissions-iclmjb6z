class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = set()

        def traverse(a: int, paren: str) -> None:
            if a == n:
                output.add(paren)
                return
            
            for i, v in enumerate(paren):
                if v == "(":
                    nu = paren[:i] + "()" + paren[i:]
                    traverse(a + 1, nu)
                    mu = paren[:i + 1] + "()" + paren[i + 1:]
                    traverse(a + 1, mu)
        traverse(1, "()")
        return list(output)

