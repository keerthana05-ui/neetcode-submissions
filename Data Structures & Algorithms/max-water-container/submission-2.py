class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0 
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            best = max(best, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best
        