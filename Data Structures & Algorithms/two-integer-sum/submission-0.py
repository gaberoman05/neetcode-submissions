class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two conditions: add to target and index is not the same (only one pair per solution)
        # Brute force = nested for loops O(n^2)
        # Initial idea: use two pointer to work through array, go to next index until there is no duplicate
        # is the list sorted initially, maybe keep track of set of tuples? if visited, skip
        # Idea: have a set of tuples that tracks which pairs have been visited. Iterate through list where i begins at 0 and j begins at i+1. Check if a tuple (nums[i], nums[j]) exists yet. If it does, increment j, otherwise, check if fits target
        pairs_set = set()
        pair = []
        for i in range(len(nums)-1):
            j = i+1
            while (not((i,j) in pairs_set) and j < len(nums)):
                if nums[i] + nums[j] == target:
                    pair.append(i)
                    pair.append(j)
                    return pair
                pairs_set.add((i,j))
                j +=1


        