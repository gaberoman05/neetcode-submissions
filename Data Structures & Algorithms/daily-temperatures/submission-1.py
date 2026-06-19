class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stack_ind = stack.pop()[1]
                result[stack_ind] = i-stack_ind
            stack.append([temperatures[i],i])
        return result

            