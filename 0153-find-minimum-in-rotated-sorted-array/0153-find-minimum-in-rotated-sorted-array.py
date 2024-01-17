class Solution:
    def findMin(self, nums: List[int]) -> int:
        times_rotated = 0
        for item in range(len(nums)):
            if item!=len(nums)-1 and nums[item]>nums[item+1]:
                times_rotated = item + 1
                break
        # l,r = 0,len(nums)-1
        # mid = (l+r)//2
        # while l<=r:
        #     mid = (l+r)//2
        #     if mid
        return nums[times_rotated]