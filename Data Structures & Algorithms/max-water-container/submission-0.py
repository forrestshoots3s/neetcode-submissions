class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = i
        r = lens(heights) - 1
        while l < r:
            if heights[l] * heights[r] > area:
                area = heights[l] * heights[r]
            if heights[l] < heights[r]:
                l += 1
            if heights[l] > height[r]:
                r -= 1