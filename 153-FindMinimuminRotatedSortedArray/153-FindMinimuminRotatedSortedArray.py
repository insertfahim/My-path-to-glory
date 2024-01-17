class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                minimum = min(minimum,nums[l])
            mid = (l+r)//2
            minimum = min(minimum,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r = mid-1
        return minimum
                
        
[3,4,5,1,2]
