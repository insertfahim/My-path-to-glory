class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1
        while l<r:
            width  = r-l
            heightt = min(height[l],height[r])
            area = width*heightt
            max_area = max(area,max_area)
            if height[l]<=height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
        return max_area
        
        