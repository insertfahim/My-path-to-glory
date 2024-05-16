class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left,right=0,len(height)-1
        leftmax=height[0]
        rightmax=height[-1]
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                res+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                res+=rightmax-height[right]
        return res