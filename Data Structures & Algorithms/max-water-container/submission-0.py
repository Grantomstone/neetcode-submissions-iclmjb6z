class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            minimum = min(heights[l], heights[r])
            area = (r - l) * minimum
            #print(f"calculating area between {heights[l]} and {heights[r]} as {area}")
            maxArea = max(maxArea, area)
            if minimum == heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea