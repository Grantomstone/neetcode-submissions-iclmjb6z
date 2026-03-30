class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(':
                    stack.append('(');
                case ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case '{':
                    stack.append('{');
                case '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                case '[':
                    stack.append('[');
                case ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                case _:
                    continue
        if not stack:
            return True
        return False

        