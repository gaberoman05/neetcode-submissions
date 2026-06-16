class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First mistake: not fully reading question and undertanding task
        # Initial idea: empty list to begin with,. Sort. 
        nums.sort()
        longest_list = []
        running_list = []
        if len(nums)>0:
            longest_list = [nums[0]]
            running_list = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif (not ((nums[i]) == nums[i-1]+1)):
                running_list = [nums[i]]
            else:
                running_list.append(nums[i])
            if len(running_list) > len(longest_list):
                longest_list = running_list
        return len(longest_list)
                