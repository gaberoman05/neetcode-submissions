class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea - iterate through list and make hash map where key is value, and value is index
        # iterate through again and check for value 
        index_map = dict()
        for i in range(len(nums)):
            index_map[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_map and i !=index_map[difference]:
                return [min(i,index_map[difference]), max(i, index_map[difference])]
        