class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
        if c>1:
            return False
        if c==1 and nums[0]<nums[len(nums)-1]:
            return False
        return True