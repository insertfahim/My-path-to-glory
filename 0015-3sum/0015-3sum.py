class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]+num>0:
                    r-=1
                elif nums[l]+nums[r]+num<0:
                    l+=1
                elif nums[l]+nums[r]+num==0:
                    res.append([nums[r],nums[l],num])
                    l+=1
                    r-=1
                    while nums[r]==nums[r+1] and r>l:
                        r-=1
        return res