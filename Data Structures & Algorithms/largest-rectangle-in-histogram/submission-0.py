class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = -1

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                topIndex, topHeight = stack.pop()
                area = topHeight * (index - topIndex)
                maxArea = max(area, maxArea)
                start = topIndex
            stack.append((start, height))

        stackLength = len(heights)
        for index, height in stack:
            maxArea = max(maxArea, height * (stackLength - index))
        
        return maxArea

        