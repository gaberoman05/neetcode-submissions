class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # pseudo code
        # iterate through list
        # check if element is in hash set, if is return true
        # if not, add
        # return False outside of loop
        unique_nums = set()
        for num in nums:
            if (num in unique_nums):
                return True
            else:
                unique_nums.add(num)
        return False
        