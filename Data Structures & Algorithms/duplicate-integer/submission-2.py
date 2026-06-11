class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution one (sort): sort array and iterate through array. At any point if next index is == return false
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        # Solution two (hash set): check if key is in hashset, if not add, if it is, return true 
        