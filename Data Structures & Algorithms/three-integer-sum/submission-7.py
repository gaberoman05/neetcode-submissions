class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it
        # outer loop to handle Left
        # inner loop to handle middle and right which try to find a sum of -nums[L]
        # inner m will move right if sum is too small, r if too big
        nums.sort()
        ret = []
        l = 0
        while l < len(nums) - 2:
            r = len(nums) - 1
            m = l + 1
            while m < r:
                mid_sum = nums[m] + nums[r]
                if mid_sum + nums[l] == 0:
                    ret.append([nums[l], nums[m], nums[r]])
                    last_m = nums[m]
                    last_r = nums[r]
                    m += 1
                    r -= 1
                    while m < r and nums[m] == last_m:
                        m += 1
                    while m < r and nums[r] == last_r:
                        r -= 1
                elif mid_sum > -nums[l]:
                    r -= 1
                else:
                    m += 1
            l += 1
            while l < len(nums) - 2 and nums[l] == nums[l-1]:
                l += 1
        return ret
                

        