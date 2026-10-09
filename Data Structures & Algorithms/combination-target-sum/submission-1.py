class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        # base case, choices, constraints, backtracking step
        def backtrack(index, path, total):

            if total == target:
                results.append(path[:])
                return
            if total > target or index >= len(nums):
                return
            
            # include nums[index], stay at same index to allow reuse
            path.append(nums[index])
            backtrack(index, path, total + nums[index])
            path.pop()
            
            # skip to next index
            backtrack(index + 1, path, total)
            
        backtrack(0,[],0)
        return results
            