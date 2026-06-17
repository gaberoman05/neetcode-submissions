class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initial idea: start with two pointers on opposite ends. Decrease each side (one at atime)
        # Calc area (distance between indexes and the min of the two vals at the indexes), keep a running max
        start = 0
        end = len(heights) - 1
        max_a = 0
        while start < end:
            if (end-start)*min(heights[start],heights[end]) > max_a:
                max_a = (end-start)*min(heights[start],heights[end])
            if heights[start] > heights[end]:
                end -= 1
            elif heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
                start += 1
        return max_a

