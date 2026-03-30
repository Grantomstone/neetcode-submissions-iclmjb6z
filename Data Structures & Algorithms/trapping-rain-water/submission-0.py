class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        area = 0

        while l < r:
            if maxl > maxr:
                r -= 1
                maxr = max(height[r], maxr)
                area += maxr - height[r]
            else:
                l += 1
                maxl = max(height[l], maxl)
                area += maxl - height[l]
        
        return area