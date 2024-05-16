class Solution:
    def trap(self, height: List[int]) -> int:
        pool = 0
        max_left = []
        max_right= []
        left  = 0
        right = 0
        for bar in height:
            max_left.append(left)
            left = max(left,bar)
        for bar in height[::-1]:
            max_right.insert(0,right)
            right = max(right,bar)
        for i in range(len(height)):
            water = min(max_left[i],max_right[i])-height[i]
            if water>0:
                pool+=water
        return pool