class Solution:
    def trap(self, height: List[int]) -> int:
        pool = 0
        left_right = []
        left  =  0
        right = 0
        for bar in height:
            left_right.append(left)
            left = max(left,bar)
        for bar in range(-1,-len(height),-1):
            left_right[bar]=min(right,left_right[bar])
            right = max(right,height[bar])
        for i in range(len(height)):
            water = left_right[i]-height[i]
            if water>0:
                pool+=water
        return pool