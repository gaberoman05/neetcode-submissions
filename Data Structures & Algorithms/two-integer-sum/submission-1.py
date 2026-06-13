class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initial idea: iterate through one of lists and create a hashmap where each key is target-list[i] and val is i.
        # Then iterate through other list checking if target in hashmap 
        """
        target_nums = {target-nums[0]: 0}
        ret = []
        for i in range(1,len(nums)):
            target_difference = target - nums[i]
            if (target_nums[target_difference] > i):
                target_nums[target_difference] = i
        
        for j in range(len(nums)):
            if (nums[j] in target_nums):
                if j > target_nums[j]:
                    ret = [target_nums[j],j]
                else:
                    ret = [j, target_nums[j]]
        return ret
        """
        # Approach 2 (after 22 mins)
        # Idea: Create a duplicate list where each item is target-num, then turn list into hash, where key is target-num and val is index
        diff_dict = dict()
        ret = []
        for i in range(len(nums)):
            target_diff = target - nums[i]
            if target_diff not in diff_dict:
                diff_dict[target_diff] = i
        for j in range(len(nums)):
            if (nums[j] in diff_dict):
                if j > diff_dict[nums[j]]:
                    ret = [diff_dict[nums[j]],j]
                else:
                    ret = [j, diff_dict[nums[j]]]
        return ret

        # Approach 3 (memorized)
        # Sort