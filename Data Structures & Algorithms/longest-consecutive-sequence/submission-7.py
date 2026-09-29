class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting is the first thing to do
        # removing duplicates
        # set and sorting
        nums = sorted(set(nums))
        max_sequence = 0
        current_sequence = 1
        i = 1
        for i in range(len(nums)):
            if nums[i-1]+1 == nums[i]:
                current_sequence += 1
            else:
                current_sequence = 1
            if current_sequence > max_sequence:
                max_sequence = current_sequence
        return max_sequence 
