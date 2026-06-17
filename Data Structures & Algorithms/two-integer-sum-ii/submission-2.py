class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Notes: non-decreasing order, that means start at left and work way up, if sum surpasses, something needs to work back
        # Use subtraction. First pointer (subtractor) iterate over until difference has been met or if exceed
        # if exceeded, incerement difference pointer  and reset pointer to +1 of difference.
        for i in range(len(numbers)-1):
            tracer_ind = i + 1
            difference = target - numbers[i]
            while tracer_ind < len(numbers):
                if numbers[tracer_ind] > difference:
                    break
                elif numbers[tracer_ind] == difference:
                    return [i+1,tracer_ind+1]
                else:
                    tracer_ind += 1
        return []