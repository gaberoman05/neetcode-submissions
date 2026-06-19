class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = int(tokens[0])
        stack = []
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if tokens[i] == "+":
                stack.pop()
                total = int(stack.pop()) + int(stack.pop())
                print(total)
                stack.append(total)
            elif tokens[i] == "-":
                stack.pop()
                total = -(int(stack.pop()) - int(stack.pop()))
                print(total)
                stack.append(total)
            elif tokens[i] == "*":
                stack.pop()
                total = int(stack.pop())* int(stack.pop())
                print(total)
                stack.append(total)
            elif tokens[i] == "/":
                stack.pop()
                divisor = int(stack.pop())
                dividend = int(stack.pop())
                total = int(dividend/divisor)
                print(total)
                stack.append(total)
        return total
