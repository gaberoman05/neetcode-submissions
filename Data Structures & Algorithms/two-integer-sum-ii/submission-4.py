class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        base_ind = 0
        tracer_ind = 1
        while base_ind < len(numbers)-1:
            difference = target - numbers[base_ind]
            if tracer_ind == len(numbers):
                base_ind += 1
                tracer_ind = base_ind +1
            elif numbers[tracer_ind] == difference:
                return [base_ind + 1, tracer_ind +1]
            else:
                tracer_ind += 1
        