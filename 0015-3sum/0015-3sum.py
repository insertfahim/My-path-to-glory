class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for index,num1 in enumerate(nums):
            if index>0 and nums[index-1]==num1:
                continue
            left,right = index+1,len(nums)-1
            while left<right:
                threeSum = num1+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    res.append([num1,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res