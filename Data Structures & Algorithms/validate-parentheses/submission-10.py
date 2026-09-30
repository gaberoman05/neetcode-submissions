class Solution:
    def isValid(self, s: str) -> bool:
        # stack for LIFO
        stack = []
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif char in {')', '}', ']'}:
                if stack:
                    if char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True

