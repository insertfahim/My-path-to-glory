class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total, res = 0, 0
        l, r = 0, 0
        while r<len(nums):
            total+=nums[r]
            while nums[r]*(r-l+1)>k+total:
                total-=nums[l]
                l+=1
            res = max(res,(r-l+1))
            r+=1
        return res
        