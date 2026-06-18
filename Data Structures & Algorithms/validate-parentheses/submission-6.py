class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ["{}", "[]", "()"]
        if len(s)%2 == 1:
            return False
        stack = []
        for i in range(len(s)):
            if (not stack):
                stack.append(s[i])
            else:
                if stack[-1]+s[i] in pairs:
                    stack.pop()
                else:
                    stack.append(s[i])
        return (not stack)