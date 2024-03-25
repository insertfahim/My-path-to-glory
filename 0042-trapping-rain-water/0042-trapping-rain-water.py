class Solution:
    def trap(self, height: List[int]) -> int:
        min_l_r = []
        max_l = 0
        max_r = 0
        res = 0
        for h in height:
            min_l_r.append(max_l)
            max_l = max(max_l,h)
        for h in range(len(height)-1,-1,-1):
            min_l_r[h]=min(min_l_r[h],max_r)
            max_r = max(max_r,height[h])
        for i in range(len(min_l_r)):
            cals =min_l_r[i]-height[i]
            if cals>0:
                res+=cals
            # res+=min_l_r[i]-height[i] if min_l_r[i]-height[i]>0 else 0
            # min_l_r[i]=min_l_r[i]-height[i]
        return res
        