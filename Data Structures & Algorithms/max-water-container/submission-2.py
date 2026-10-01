class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            if heights[l] * heights[r] > area:
                area = heights[l] * heights[r]
            if heights[l] < heights[r]:
                l += 1
            if heights[l] > height[r]:
                r -= 1
        return area