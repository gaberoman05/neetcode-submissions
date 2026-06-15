class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        
        ret_list = [0]*len(nums)

        prod = 0
        mult_b = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                mult_a = nums[i]
                prod = mult_a*mult_b
                mult_b = prod
            else:
                zero_ind = i
            
        
        if zero_count == 1:
            ret_list[zero_ind] = prod
        elif zero_count == 0:
            for i in range(len(nums)):
                ret_list[i] = prod//nums[i]
        return ret_list



        