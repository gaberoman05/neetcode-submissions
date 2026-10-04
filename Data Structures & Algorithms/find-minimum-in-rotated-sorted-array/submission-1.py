class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the number where nums[i] > nums[i+1]
        l = 0
        r = len(nums)-1
        m = 0
        while l <= r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[m] 